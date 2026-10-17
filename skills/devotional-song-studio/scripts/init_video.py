#!/usr/bin/env python3
"""Create a dedicated video workspace without overwriting existing artifacts."""

import argparse
import json
from pathlib import Path
import re


def slug(value):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', value):
        raise argparse.ArgumentTypeError('Use lowercase letters/digits separated by hyphens')
    return value


def initialize(workspace, song_slug, video_slug):
    song_slug, video_slug = slug(song_slug), slug(video_slug)
    workspace = Path(workspace).resolve()
    target = workspace / 'productions' / song_slug / 'videos' / video_slug
    # Resolve existing symlinks before creating anything to prevent escaping ownership.
    if not target.resolve().is_relative_to(workspace):
        raise ValueError('Video folder resolves outside the workspace')
    folders = ('audio', 'assets', 'analysis', 'project', 'previews', 'exports', 'release')
    for folder in folders:
        if not (target / folder).resolve().is_relative_to(target.resolve()):
            raise ValueError('A video subfolder resolves outside its video folder')
    target.mkdir(parents=True, exist_ok=True)
    for folder in folders:
        (target / folder).mkdir(exist_ok=True)
    manifest = target / 'video.json'
    if manifest.is_symlink():
        raise ValueError('Refusing a symlinked video manifest')
    try:
        with manifest.open('x', encoding='utf-8') as output:
            json.dump({'schema_version': 1, 'song_slug': song_slug,
                       'video_slug': video_slug, 'stage': 'created',
                       'selected_audio': None, 'timing_review': 'pending',
                       'artifacts': {}, 'unresolved': []}, output, indent=2)
            output.write('\n')
    except FileExistsError:
        pass
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, default=Path.cwd())
    parser.add_argument('--song-slug', type=slug, required=True)
    parser.add_argument('--video-slug', type=slug, required=True)
    args = parser.parse_args()
    try:
        target = initialize(args.workspace, args.song_slug, args.video_slug)
    except (OSError, ValueError) as exc:
        parser.exit(1, f'Cannot initialize video: {exc}\n')
    print(json.dumps({'video_folder': str(target), 'status': 'ready'}))


if __name__ == '__main__':
    main()
