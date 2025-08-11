# Hey Professor — Multi-language Jarvis (Demo)
This package contains a demo multi-language assistant named "Hey Professor".
It is a starter-pack: backend (FastAPI), a simple frontend, STT (OpenAI Whisper), and TTS (ElevenLabs / pyttsx3 fallback).

## What's included
- backend/main.py: FastAPI app with WebSocket chat and /voice endpoint
- backend/assistant.py: Assistant wrapper that calls OpenAI (if API key provided)
- backend/stt.py: Uses OpenAI Whisper API if key present
- backend/tts.py: Calls ElevenLabs if key present, otherwise uses pyttsx3
- frontend/index.html: Simple chat UI with file upload for audio (.wav)
- requirements.txt: Python dependencies
- .env.example: Example environment variables
- wake_listener.py: Stub/instructions for wake-word 'Hey Professor'

## Quick start
1. Extract the zip.
2. Create and activate a Python virtual environment (Python 3.10+ recommended).
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your API keys.
5. Run the backend:
   ```
   uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
   ```
6. Open the frontend in a browser:
   ```
   http://localhost:8000/static/index.html
   ```
7. For voice tests: record a `.wav` file and upload via the file input. (Full browser mic capture will require extra client-side code and CORS handling.)

## Notes
- This is a starter/demo package. For production use add authentication, command whitelisting, secure key management, and better audio handling.
- Wake-word setup (Hey Professor) is optional — check Picovoice/Porcupine or Vosk for offline detection and follow their docs.

## Need help?
Reply in this chat and I will help you run it, or I can customize further (React UI, live mic recording, WhatsApp integration, deploy to VPS).
