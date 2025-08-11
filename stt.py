import os
import openai

def transcribe_audio(filepath: str) -> str:
    """Transcribe audio using OpenAI Whisper API if OPENAI_API_KEY is set.
    Fallback returns empty string if not available.
    """
    key = os.getenv("OPENAI_API_KEY")
    if key:
        try:
            with open(filepath, "rb") as f:
                resp = openai.Audio.transcriptions.create(
                    file=f,
                    model="whisper-1"
                )
            return resp.get("text","")
        except Exception as e:
            return ""
    else:
        # No API key: return empty or simple notice
        return ""
