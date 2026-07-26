from app.voice.recognizer import SpeechRecognizer

recognizer = SpeechRecognizer()

text = recognizer.transcribe("recording.wav")

print()
print("Recognized:")
print(text)