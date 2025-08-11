from fastapi import FastAPI, WebSocket, UploadFile, File
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import json
import asyncio
import os
from assistant import Assistant

load_dotenv()
app = FastAPI()
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

assistant = Assistant()

@app.get("/health")
async def health():
    return {"status": "Hey Professor Jarvis backend running"}

@app.websocket("/ws/chat")
async def websocket_chat(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_text()
            msg = json.loads(data)
            if msg.get("type") == "user_message":
                user_text = msg["text"]
                reply = await assistant.chat(user_text)
                await ws.send_text(json.dumps({"type":"assistant_message","text":reply}))
    except Exception:
        await ws.close()

@app.post("/voice")
async def voice_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    reply_text = await assistant.handle_audio(audio_bytes)
    return {"text": reply_text}
