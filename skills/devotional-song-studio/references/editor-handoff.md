# Resume and recover in another AI code editor

Use when moving a project to another editor or when the current HyperFrames skills cannot be found. The editable project is portable; skill discovery and installed tools vary by editor.

## Establish the resume point

Read the repository's SKILL.md and studio-preferences.md, then production.json, video.json, the owning workflow's BRIEF.md, motion.md, and the latest review. Identify selected audio hash, last good export, current defects, and requested scope before making changes. Keep completed work when a tool is unavailable. Use absolute resolved paths for invoking this skill's Python scripts; use relative project-local paths in deliverables.

For a lyric-only revision, save a new draft or diff and retain the performed transcript and locked audio/video. A draft revision does not invalidate unchanged rendered media; label the new words as not yet performed. Invalidate downstream timing only when the selected audio actually changes.

For motion-only revisions, preserve the soundtrack and reviewed cues. Inspect the existing timeline through the loaded current CLI when available. Keep previous source/export versions reviewable.

## Recover the installed HyperFrames instructions

Check the editor's actual skill/plugin catalog and project/global instruction locations; do not assume a Codex path or slash command exists in every editor.

**Plugin installation:** locate the installed HyperFrames entry SKILL.md and read its bundled `references/plugin-installation.md`, resolved relative to that entry inside the same plugin. If the entry cannot be found, report that missing installation. The plugin manager owns its skills and version. Resolve the entry and domains within the same bundle and use its launcher. If a required bundled skill is absent, report that exact missing resource; do not mix in a different standalone release or modify plugin files.

**Standalone installation:** the [official skills guide](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/skills.mdx) documents these commands, checked 2026-10-17:

```bash
npx hyperframes skills check --json
npx hyperframes skills update
```

The first inspects installation freshness; the second installs/refreshes core skills and existing workflows. Installation can write outside the project and needs network access, so follow the environment's execution permissions and existing setup authorization. If the installed skill adds an explicit update approval requirement, follow it. Once available, read the entry skill and let it select/install the owning workflow. Do not preinstall every workflow.

When discovery still fails, refresh/reload the editor's skills or start a new session as its own documentation directs. Directly reading the correct installed SKILL.md is sufficient if automatic skill discovery is the only missing feature. Do not reconstruct missing runtime contracts from memory.

If setup cannot complete, continue independent lyrics, story, image prompts, and motion planning. Report the exact failed command/missing file and next action; leave rendering status unverified. Do not regenerate the song or migrate away from HyperFrames to work around editor setup.

## Handoff note

Record selected master identity, project and skill/runtime versions, last validated command, known defects/timecodes, pending work, and how to run the existing project from its project directory. Keep prompts and downloaded assets, exclude credentials/browser profiles, and retain the lockfile. Never label planned timestamps or a written scene plan as inspected video.
