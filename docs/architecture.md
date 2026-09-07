# Architecture

## Briefing pipeline

```mermaid
flowchart LR
    A[CLI / notebook / local Gradio UI] --> B[Validate video URL and settings]
    B --> C[yt-dlp metadata and duration check]
    C --> D[Download and FFmpeg MP3 conversion]
    D --> E[Check file size]
    E --> F[OpenAI transcription]
    F --> G[Check transcript length]
    G --> H[OpenAI structured briefing]
    H --> I[Display or save summary]
```

`app.py` owns presentation and translates known errors into UI messages. `summarizer.py` owns validation, resource bounds, provider interaction, and orchestration. `YT_Summarizer.ipynb` imports this same implementation so fixes are not duplicated across notebook cells.

Each request gets its own `TemporaryDirectory`. Its contents are removed when the request completes or raises, and the OpenAI client is closed. Audio is never deliberately persisted. Abrupt process termination can leave operating-system temporary files; there is no background cleanup service. The transcript and summary live in process memory, with only the CLI's explicit `--output` option writing a briefing.

## External boundaries

- YouTube/yt-dlp provides metadata and downloads media. Video URLs are normalized to a known YouTube watch URL; playlists and arbitrary external URLs are rejected. The service can still restrict automated downloads.
- FFmpeg and ffprobe are local executables responsible for audio conversion and inspection.
- OpenAI receives the audio for transcription, then receives the transcript and title for summarization. The project does not make claims about provider data retention.
- Gradio serves a local browser interface. Its own framework behavior and dependencies are separate from the pipeline; no public deployment has been audited.

The model receives fixed briefing rules in a system message and source material in a user message. Treating transcript instructions as data reduces accidental instruction following, but is not a proof of prompt-injection resistance or factual accuracy. The model has no tools or application actions to invoke.

## Bounds and failures

The implementation validates duration before downloading, applies yt-dlp's 24 MB source-file bound, and checks converted file size before uploading. This bounds accepted files, not total memory, disk, elapsed time, or API spending. The provider client has a 180-second request timeout and one retry; the downloader uses a 30-second socket timeout and two retries. Jobs have no end-to-end deadline or cancellation API. At most one UI job runs concurrently.

Known provider authentication, quota, and API errors get concise messages without raw request details. A truncated or otherwise unfinished summary is treated as failure. Large-audio segmentation and multi-stage long-transcript summarization are not implemented in the maintained pipeline.

## Retrieval lab

`MIT COCOMELON.ipynb` demonstrates clean text → overlapping word chunks → normalized Sentence Transformer vectors → FAISS inner-product search. It uses `sentence-transformers/all-MiniLM-L6-v2` and an in-memory index for one transcript. Searches clamp `top_k` to available chunks and reject invalid input. Indexes are rebuilt when text changes and disappear with the kernel.

This experiment does not generate question answers, cite timestamps, persist indexes, or participate in the briefing pipeline. The word-based chunker is a teaching implementation; model-token-aware chunking and relevance evaluation remain future work.
