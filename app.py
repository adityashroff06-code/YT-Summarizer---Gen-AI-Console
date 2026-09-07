"""Launch the local Gradio console: python app.py."""
from dotenv import load_dotenv
import gradio as gr

from summarizer import SummarizerError, summarize_youtube_video


def summarize_bot(url: str, language: str) -> str:
    try:
        return summarize_youtube_video(url, language=language)
    except SummarizerError as exc:
        raise gr.Error(str(exc)) from None
    except Exception:
        # Do not expose upstream request details or local file paths in the UI.
        raise gr.Error("The request failed. Check your connection and retry with a short public video.") from None


def create_app():
    return gr.Interface(
        fn=summarize_bot,
        inputs=[
            gr.Textbox(label="YouTube video URL", placeholder="https://www.youtube.com/watch?v=..."),
            gr.Textbox(label="Spoken language (optional)", placeholder="en, hi, fr; leave blank to detect"),
        ],
        outputs=gr.Textbox(label="Video briefing", lines=24),
        title="GenAI Video Briefing Console",
        description=(
            "Turn spoken video content into an executive summary, key ideas, actionable "
            "takeaways, and a one-sentence TL;DR. Audio and transcript are sent to OpenAI "
            "using your configured API key. Start with a short public video; review the "
            "brief against the source before relying on it."
        ),
        flagging_mode="never",
    )


if __name__ == "__main__":
    load_dotenv()
    create_app().queue(default_concurrency_limit=1, max_size=8).launch(
        server_name="127.0.0.1", share=False, show_error=False
    )
