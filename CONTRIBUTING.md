# Contributing

Start with the [setup guide](docs/setup.md), then keep each change focused on a reproducible problem. Describe the trigger, expected behavior, and actual behavior in an issue or pull request. Do not include credentials or private media.

## Development checks

```sh
python -m unittest discover -s tests -v
python summarizer.py --help
python -c "from app import create_app; create_app().close()"
```

Install `requirements.txt` before the UI check. Core tests use the Python standard library and fake external services; no API key or media download is needed. Follow [validation](docs/validation.md) for manual integration checks.

When changing orchestration, cover the relevant success/failure boundaries: URL normalization, no download after invalid metadata, no upload after oversized audio, handling incomplete model responses, and cleanup on failure. Keep UI code thin and reuse `summarizer.py` from notebooks. Avoid model claims that are not supported by an evaluation.

Before submitting, clear notebook outputs and execution counts, run `git diff --check`, and confirm no `.env`, generated media, transcripts, or keys are staged. Update the README or relevant guide when behavior/configuration changes. Do not add an invented license, badge result, screenshot, benchmark, or production-readiness claim. License selection remains the repository owner's decision.
