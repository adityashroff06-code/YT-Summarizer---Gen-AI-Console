# Setup

## Requirements

Use Python 3.11–3.13 and a virtual environment. Python 3.13 on Windows is the local verification environment; the automated workflow also declares Python 3.11 and 3.12 jobs. The application requires network access to YouTube and OpenAI. The retrieval notebook additionally downloads an embedding model from Hugging Face.

Install the Python dependencies from the repository root:

```sh
python -m venv .venv
# Activate .venv as shown in the README.
python -m pip install -r requirements.txt
```

Dependency ranges bound major upgrades; they are not a complete reproducible lockfile. See [validation](validation.md) for the versions used during the local check. Revalidate before changing versions.

## FFmpeg

Install FFmpeg from your operating system's package manager or the [official FFmpeg download page](https://ffmpeg.org/download.html). On Windows, add the extracted `bin` directory to your user PATH and reopen the terminal. Both executables must resolve:

```sh
ffmpeg -version
ffprobe -version
```

A Python package named `ffmpeg` is not a replacement for these executables. A local FFmpeg install is needed even though the transcription runs remotely.

## Credentials

Copy `.env.example` to `.env`, then put your own API key after `OPENAI_API_KEY=`. The app and CLI load `.env` automatically; existing process environment values take precedence. Python callers should call `dotenv.load_dotenv()` themselves or supply environment variables before invoking the pipeline.

Do not put keys into shell commands saved in history, notebook source, screenshots, or issue reports. Earlier notebook revisions contained a literal credential. Removing that text from the current version does not revoke the key or remove historical copies. The account owner must revoke the exposed credential; see [security guidance](../SECURITY.md).

## Start and stop

```sh
python app.py
```

Use the URL printed at launch. Only the local machine is exposed by default. Stop with Ctrl+C. No public sharing endpoint, login, persistent job store, or application authentication is configured.

If PowerShell blocks activation, use `.\.venv\Scripts\python.exe` directly for commands instead of changing the machine's execution policy.

## Notebooks

```sh
python -m pip install -r requirements-notebooks.txt
python -m jupyter lab
```

Start from the repository root and select the environment's Python kernel. `YT_Summarizer.ipynb` is the application walkthrough. `MIT COCOMELON.ipynb` is an independent retrieval experiment and needs more RAM/disk for its model and ML packages. Neither notebook enables a public Gradio sharing link. Clear outputs before committing.
