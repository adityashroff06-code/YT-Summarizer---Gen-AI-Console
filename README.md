# GenAI Video Briefing Console

Turn a spoken YouTube video into an executive summary, key ideas, actionable takeaways, and a one-sentence TL;DR.

The project combines **yt-dlp**, **OpenAI transcription**, and a **Gradio interface**. A command-line entry point and a guided notebook use the same pipeline. A separate retrieval lab explores Sentence Transformers and FAISS.

**Status:** a local application for personal use and demonstrations, with automated offline regression checks. Live YouTube/OpenAI behavior and briefing quality require an integration check with your own API account. This is not a hosted, multi-user service.

## Quick start

Prerequisites: Python 3.11–3.13, Git, FFmpeg (including `ffprobe`) on PATH, and an OpenAI API key with access to the configured models. API usage incurs charges.

```sh
git clone https://github.com/adityashroff06-code/YT-Summarizer---Gen-AI-Console.git
cd YT-Summarizer---Gen-AI-Console
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```sh
# macOS / Linux
source .venv/bin/activate
```

Then install and configure:

```sh
python -m pip install -r requirements.txt
python -c "from pathlib import Path; p=Path('.env'); p.exists() or p.write_text(Path('.env.example').read_text())"
```

Open `.env` in your editor and set `OPENAI_API_KEY`. Keep it private. Verify FFmpeg with `ffmpeg -version` and `ffprobe -version`, then start:

```sh
python app.py
```

Open the local URL printed in your terminal. Paste a completed public YouTube video with clear speech, leave the language blank for detection, and submit. The server binds to `127.0.0.1`; public sharing is disabled.

For a command-line briefing:

```sh
python summarizer.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --output artifacts/brief.md
```

Replace `YOUR_VIDEO_ID` with an actual video ID. See [setup](docs/setup.md) for FFmpeg installation and [usage](docs/usage.md) for notebooks and configuration.

## What it does

- Accepts watch, short-link, Shorts, embed, and completed live-video URLs; removes playlist and tracking parameters.
- Downloads a single video's audio and converts it to MP3 with the correct extension.
- Transcribes speech and produces four consistent briefing sections.
- Applies duration, audio-size, and transcript-length bounds with actionable errors.
- Cleans temporary audio after success or failure.
- Keeps API credentials outside notebook source and version control.

The default limit is **30 minutes**; the original downloaded audio and converted upload must fit the **24 MB** file bound. Some shorter videos may exceed that bound. Visual content, slide text, speaker labels, timestamps, live streams, private videos, batch jobs, and persistent history are not supported. Generated summaries can contain errors; compare consequential claims with the original video.

## Project map

| Path | Purpose |
| --- | --- |
| [`app.py`](app.py) | Local Gradio interface |
| [`summarizer.py`](summarizer.py) | Shared pipeline and CLI |
| [`YT_Summarizer.ipynb`](YT_Summarizer.ipynb) | Guided notebook using the shared pipeline |
| [`MIT COCOMELON.ipynb`](MIT%20COCOMELON.ipynb) | Separate semantic-search learning experiment |
| [`tests/`](tests/) | Offline boundary and failure-path regression checks |
| [`docs/`](docs/) | Setup, usage, architecture, troubleshooting, and validation |

The pre-existing meeting recording is retained as a historical repository asset. The application does not read it and it is not a test fixture.

## Documentation

[Setup](docs/setup.md) · [Usage and configuration](docs/usage.md) · [Architecture](docs/architecture.md) · [Troubleshooting](docs/troubleshooting.md) · [Validation](docs/validation.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md)

## Development

Run the network-free checks with standard Python:

```sh
python -m unittest discover -s tests -v
python summarizer.py --help
```

The CI workflow runs these checks and constructs the Gradio app after installing dependencies. Tests replace providers with fakes; they do not download media, call paid APIs, or measure summary quality.

## License

No license has been selected for this repository. Do not infer an open-source license from its public visibility or the retrieval notebook's filename. The owner must choose the intended reuse terms; third-party libraries and media retain their own terms.
