# Troubleshooting

| Symptom | Action |
| --- | --- |
| `OPENAI_API_KEY` missing | Set a nonempty key in `.env` and run from the repository root. Restart a running app after configuration changes. |
| Authentication failure | Verify the key belongs to the intended project and is active. Never paste it into an issue. |
| OpenAI rate or billing limit | Check your API account's available credit, project limits, and model access; retry later if rate-limited. |
| FFmpeg/ffprobe missing | Install the executables, add their directory to PATH, and reopen the terminal. |
| YouTube download fails | Check that the video is public, completed, playable from your network, and permitted for you to process. YouTube may require a supported JavaScript runtime or impose automated-access restrictions; consult [yt-dlp's installation guidance](https://github.com/yt-dlp/yt-dlp#installation). No cookie or restriction-bypass flow is provided. |
| Source audio over 24 MB | Try a shorter video. The downloaded source and converted upload are both bounded, so changing only the duration limit may not help. |
| Live/upcoming video rejected | Wait until a completed, downloadable recording is available. |
| Invalid video URL | Use a complete watch, short-link, Shorts, embed, or completed live-video URL. Playlist-only and non-YouTube URLs are rejected. |
| Transcript empty | Choose clear speech and an appropriate language code, or allow automatic detection. Music/silence is not useful input. |
| Transcript too long | Use a shorter video. The app does not silently truncate text or split it into summary jobs. |
| Incomplete briefing/model error | Try the documented model defaults and a shorter input. Alternative models may not support the same parameters. |
| Notebook imports fail | Select the virtual environment's kernel and run Jupyter from the repository root. Install `requirements-notebooks.txt` and restart the kernel. |
| Retrieval model download fails | Check Hugging Face connectivity and disk capacity. This does not affect the main briefing app. |

The app makes no guarantee of access to every public video. Keep [yt-dlp](https://github.com/yt-dlp/yt-dlp) updated within the supported dependency range when extraction changes, and rerun local checks after upgrading.

For a useful bug report, include Python/OS versions, package versions, the entry point used, and a redacted error message. Use a public reproduction video only if you can share it. Exclude API keys, cookies, private recordings, and transcripts.
