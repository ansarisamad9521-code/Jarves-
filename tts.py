import os
from dotenv import load_dotenv
load_dotenv()
ELEVEN_KEY = os.getenv("ELEVENLABS_API_KEY")

def speak_text(text: str):
    # If ElevenLabs key is present, attempt simple REST call (user must configure voice id)
    if ELEVEN_KEY:
        try:
            import requests
            voice_id = os.getenv("ELEVEN_VOICE_ID","EXAMPLE_VOICE_ID")
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
            headers = {"xi-api-key": ELEVEN_KEY, "Content-Type": "application/json"}
            data = {"text": text}
            r = requests.post(url, json=data, headers=headers)
            if r.status_code == 200:
                path = "/tmp/jarvis_reply.mp3"
                with open(path, "wb") as f:
                    f.write(r.content)
                # play using pydub if available
                try:
                    from pydub import AudioSegment
                    from pydub.playback import play
                    song = AudioSegment.from_file(path, format="mp3")
                    play(song)
                except Exception:
                    pass
        except Exception:
            pass
    else:
        # fallback to pyttsx3
        try:
            import pyttsx3
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass
