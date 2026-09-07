# Usage and configuration

## Local console

1. Start `python app.py` and open the printed local URL.
2. Paste one completed public YouTube video URL containing speech.
3. Optionally enter a two-letter spoken-language code such as `en` or `hi`. Blank lets the transcription service detect language.
4. Submit and wait for the briefing. Review it against the source and copy the text you want to keep.

The interface runs one job at a time with a queue of up to eight pending jobs. Repeating a request repeats downloading, transcription, and summarization; there is no cache. The language field describes the speech, not a requested summary translation.

## Command line

```sh
python summarizer.py "https://youtu.be/YOUR_VIDEO_ID"
python summarizer.py "https://www.youtube.com/watch?v=YOUR_VIDEO_ID" --language en --output artifacts/brief.md
python summarizer.py --help
```

Use an actual video ID. Without `--output`, the summary is printed. With it, parent directories are created and the named UTF-8 file is written (an existing file is replaced). Errors use a nonzero exit status. `artifacts/` is ignored by Git because generated summaries may contain private information.

## Python

```python
from dotenv import load_dotenv
from summarizer import summarize_youtube_video

load_dotenv()
brief = summarize_youtube_video("https://youtu.be/YOUR_VIDEO_ID", language="")
print(brief)
```

For existing transcript text, use `summarize_transcript(client, transcript, title, settings)` with an OpenAI client and `Settings.from_env()`. This sends text to the configured model; it does not run the downloader or transcription step.

## Configuration

| Name | Default | Purpose |
| --- | --- | --- |
| `OPENAI_API_KEY` | Required | Your OpenAI API credential; never logged by this application |
| `OPENAI_SUMMARY_MODEL` | `gpt-4.1-mini` | Model compatible with the application's Chat Completions parameters |
| `OPENAI_TRANSCRIPTION_MODEL` | `whisper-1` | Transcription model returning a `.text` response |
| `MAX_VIDEO_MINUTES` | `30` | Positive integer duration bound checked before download |

The default summary model supports [Chat Completions](https://developers.openai.com/api/docs/models/gpt-4.1-mini), and the transcription service accepts [supported audio formats up to 25 MB](https://developers.openai.com/api/docs/guides/speech-to-text). The application uses a smaller 24,000,000-byte bound for both download and upload. Account access, rates, and costs depend on your provider account.

The transcript bound is 120,000 characters and the output token budget is 2,200. Oversized inputs and incomplete responses fail explicitly; text is not silently truncated. Changing models may require changing API parameters and limits. No automatic migration or fallback is performed.

## Example output shape

```text
1. EXECUTIVE SUMMARY
[Three to six sentences grounded in the transcript]

2. KEY IDEAS
[Up to ten supported points]

3. ACTIONABLE TAKEAWAYS
[Supported actions, or a statement that none were mentioned]

4. ONE-SENTENCE TL;DR
[One sentence capturing the main point]
```

This is a format illustration, not a generated result or quality benchmark.
