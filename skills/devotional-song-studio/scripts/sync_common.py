"""Shared local-file and numerical helpers for the synchronization tools."""

import hashlib
import json
import math
import os
from pathlib import Path
import tempfile


def finite(value, label, minimum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{label} must be a finite number')
    if minimum is not None and value < minimum:
        raise ValueError(f'{label} must be at least {minimum}')
    return float(value)


def video_root(value):
    root = Path(value).resolve()
    if not (root / 'video.json').is_file():
        raise ValueError('Initialize this dedicated video folder first (video.json missing)')
    return root


def local_path(root, value):
    path = Path(value)
    path = path if path.is_absolute() else root / path
    path = path.resolve()
    if not path.is_relative_to(root):
        raise ValueError('Video artifacts must stay inside the dedicated video folder')
    return path


def fingerprint(path):
    digest = hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def output_path(root, value):
    candidate = root / value
    local_path(root, candidate)
    for path in (candidate, *candidate.parents):
        if path == root:
            break
        if path.is_symlink():
            raise ValueError('Refusing a symlinked generated output or output directory')
    return candidate


def atomic_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    name = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8',
                                         dir=path.parent, delete=False) as output:
            name = output.name
            output.write(text)
        os.replace(name, path)
    finally:
        if name and os.path.exists(name):
            os.unlink(name)


def atomic_json(path, value):
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
