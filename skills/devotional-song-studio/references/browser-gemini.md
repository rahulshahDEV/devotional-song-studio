# Brave, Playwright, and Gemini

## Read-only preflight

Run the included helper from the workspace (substitute its resolved skill path):

```bash
python3 skills/devotional-song-studio/scripts/probe_cdp.py --endpoint http://127.0.0.1:9222
```

It checks the local CDP version endpoint without reading tabs, cookies, or chat content. Inspect the failure reason: connection refused suggests no listener; a sandbox permission error means availability could not be checked. Neither proves Brave is missing. The helper does not start Brave or install dependencies.

Prefer an already-authorized loopback CDP endpoint. If none exists, launch a separate Brave instance with a workspace profile. Do not close the user's ordinary browser or copy/extract its cookies. From the workspace root on macOS:

```bash
mkdir -p .browser-profiles/gemini
"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
  --remote-debugging-address=127.0.0.1 \
  --remote-debugging-port=9222 \
  --user-data-dir="$PWD/.browser-profiles/gemini" \
  https://gemini.google.com/
```

Use the actual executable location on other systems. Launch with a nonblocking process facility so the terminal call does not wait for the browser lifetime. Keep `.browser-profiles/` private and out of source control, archives, and exports. The profile persists login state; the user signs in manually. Do not change account security or activity settings. Do not bypass CAPTCHA or login challenges.

Install Python Playwright into a workspace virtual environment when authorized browser execution needs it:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install playwright
```

Attaching uses installed Brave, so downloading Playwright's Chromium is unnecessary. If installation is blocked, report the missing dependency and continue independent writing work.

## Attach and inspect

Use `chromium.connect_over_cdp`, which supports Chromium browsers with lower fidelity than Playwright's native protocol. Brave compatibility must be verified in this environment. Example connection pattern:

```python
from urllib.parse import urlparse
from playwright.async_api import async_playwright

async def inspect_gemini():
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp('http://127.0.0.1:9222')
        pages = [page for context in browser.contexts for page in context.pages
                 if urlparse(page.url).hostname == 'gemini.google.com']
        if len(pages) != 1:
            raise RuntimeError('Select the intended Gemini tab explicitly')
        page = pages[0]
        # Inspect visible Gemini controls now; derive locators from the live UI.
        print(await page.title())
        # Exiting Playwright disconnects this client. Leave user-owned tabs open.
```

Do not enumerate or export unrelated tabs. If multiple Gemini tabs exist, identify the intended production tab before acting. Confirm expected account context using only necessary visible UI, without logging personal identifiers. Do not create a new anonymous browser context that loses the signed-in session.

Inspect the current model picker, music tool, duration/vocal controls, and quota notices. The user's “Argon” label is unresolved until observed or clarified. Record visible labels independently from public documentation; selecting a chat model is not proof of the underlying music model. Do not claim hidden model identity.

Use accessibility roles, visible labels, and live DOM inspection to build locators. Avoid hardcoded coordinates, invented selectors, and language-specific labels without inspection. A screenshot helps diagnose layout; it is not a stable locator contract. Capture only necessary production content and store locally.

## Submission and downloads

1. Save the prompt, settings, attempt number, and a pending status before submission.
2. Select the observed music tool and agreed model/settings. Check any actionable quota or cost notice. Do not upgrade, buy, or accept a new paid plan.
3. Submit once. Wait for a visible completion/result state using bounded waits and progress updates. On timeout inspect the existing request first; an uncertain result does not authorize another submission.
4. If generation is blocked by login, challenge, missing feature, or quota, record the condition and stop submissions. If a UI action fails, inspect once and retry that interaction once; avoid click loops.
5. Use the result's actual download control. Prefer the audio-only option for audio production. Set up `page.expect_download()` around the final control that starts the download; save into the take folder. A menu-opening click may not trigger the download yet.
6. Verify the local file is nonempty and decodable with available media tooling (for example ffprobe). Check duration and whether a downloaded MP4 actually contains audio. An extension alone proves nothing.
7. Record result metadata and review the actual take. Keep the original file. Do not publish a Gemini share link merely to obtain a local artifact.

Never extract auth tokens, replay private undocumented endpoints, or store session cookies in production records. Do not close user-owned tabs/browser. On a recoverable failure leave a precise resume note and the existing result intact.

## Verified public references

Checked 2026-10-17; refresh relevant facts during production because UI and eligibility change.

- [Google: Generate music with Gemini Apps](https://support.google.com/gemini/answer/16901237?hl=en): Lyria music tool, model selection, length options, and MP3/MP4 downloads. Availability in the live account is decisive.
- [Google: Lyria 3 Pro](https://blog.google/innovation-and-ai/technology/ai/lyria-3-pro/): longer structured tracks, up to three minutes at announcement.
- [Playwright Python: connect_over_cdp](https://playwright.dev/python/docs/api/class-browsertype#browser-type-connect-over-cdp): Chromium CDP attachment and its limitations.
