import os
import openai
from dotenv import load_dotenv
from stt import transcribe_audio
from tts import speak_text

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_KEY:
    openai.api_key = OPENAI_KEY

class Assistant:
    def __init__(self):
        self.system_prompt = (
            "You are Hey Professor — a helpful, concise multi-language assistant. "
            "Reply in the user's language when possible, be polite and actionable."
        )
        self.history = []

    async def chat(self, user_text: str) -> str:
        self.history.append({"role":"user","content":user_text})
        messages = [{"role":"system","content":self.system_prompt}] + self.history[-8:]
        # Use ChatCompletion if key present; otherwise echo/fallback
        if OPENAI_KEY:
            resp = openai.ChatCompletion.create(
                model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),
                messages=messages,
                max_tokens=500,
                temperature=0.3
            )
            assistant_msg = resp["choices"][0]["message"]["content"]
        else:
            assistant_msg = "OpenAI API key not found. (Fallback) I heard: " + user_text
        self.history.append({"role":"assistant","content":assistant_msg})
        return assistant_msg

    async def handle_audio(self, audio_bytes: bytes) -> str:
        import uuid, tempfile
        tmp = tempfile.gettempdir() + f"/{uuid.uuid4()}.wav"
        with open(tmp, "wb") as f:
            f.write(audio_bytes)
        text = transcribe_audio(tmp)
        reply = await self.chat(text)
        try:
            speak_text(reply)
        except Exception:
            pass
        return reply
