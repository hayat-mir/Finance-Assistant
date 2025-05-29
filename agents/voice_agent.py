# agents/voice_agent.py

import pyttsx3
import whisper

class VoiceAgent:
    def __init__(self):
        print("Loading Whisper STT model (tiny)...")
        self.stt_model = whisper.load_model("tiny")  # 🔁 Changed from "base"
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('rate', 160)

        voices = self.tts_engine.getProperty('voices')
        if voices:
            self.tts_engine.setProperty('voice', voices[0].id)

    def transcribe_audio(self, audio_file):
        result = self.stt_model.transcribe(audio_file)
        return result["text"]

    def speak(self, text):
        print("🗣️ Speaking:", text)
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()
