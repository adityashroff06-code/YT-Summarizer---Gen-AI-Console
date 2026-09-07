# Validation

## Local verification record

Verified on 2026-09-07 using Windows and Python 3.13.9 in a fresh virtual environment.

| Check | Result |
| --- | --- |
| Install `requirements.txt` | Passed |
| `python -m pip check` | Passed; no broken requirements |
| `python -m unittest discover -s tests -v` | Passed, 16 tests |
| `python summarizer.py --help` | Passed without an API key |
| Construct and close the Gradio interface | Passed |
| Launch on localhost and fetch the page | HTTP 200; expected application title found; server then closed |
| Construct yt-dlp's configured MP3 postprocessor | Passed |
| Notebook JSON, code syntax, cleared outputs, credential-pattern checks | Passed in the test suite |
| `git diff --check` | Passed |

The installed direct dependencies were OpenAI 2.54.0, yt-dlp 2026.8.19, python-dotenv 1.2.3, and Gradio 6.26.0. The committed requirements use bounded ranges, so a future install may resolve different versions. No remote CI result is asserted by this local record.

## What the tests establish

Tests exercise accepted/rejected URLs, configuration validation, missing credentials, pre-download duration checks, audio upload bounds, empty transcription, transcript limits, incomplete model responses, source/instruction separation, output-file extension handling, provider error translation, and temporary-directory cleanup after both success and failure. The retrieval chunker is checked for invalid settings and redundant trailing overlap.

The provider objects are fakes. Passing these tests establishes local control-flow behavior, not transcription accuracy, summary quality, YouTube availability, prompt-injection resistance, or billing behavior.

## Not yet verified

- End-to-end downloads and FFmpeg conversion: FFmpeg/ffprobe were not installed in the verification environment.
- Live OpenAI transcription and summarization: no API credential was used and no paid request was made.
- Full retrieval-notebook execution and model download: ML dependencies and weights were not installed for this check.
- Hosted CI matrix runs, macOS/Linux runtime behavior, load, security, and accessibility audits.

## Manual integration check

After configuring your own key and FFmpeg, use a short public video with clear speech that you have permission to process. Check that a four-section briefing appears in the UI and CLI, compare claims against the video, confirm the chosen spoken language is handled correctly, and inspect the temporary directory for cleanup. Repeat with an unavailable video and an over-limit input to confirm the expected errors.

Record the video, duration, language, model settings, package versions, date, and observed issues in your own evaluation notes. Do not commit credentials, private transcripts, or a claim of production readiness based on one example. Broader quality claims need a representative set of videos and explicit scoring criteria.
