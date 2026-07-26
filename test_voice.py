from app.voice.microphone import Microphone
from app.voice.recognizer import SpeechRecognizer
from app.voice.wake_word_detector import WakeWordDetector

from app.parser.command_parser import CommandParser
from app.core.command_engine import CommandEngine


microphone = Microphone()
recognizer = SpeechRecognizer()
detector = WakeWordDetector()

parser = CommandParser()
engine = CommandEngine()


while True:

    input("\nPress ENTER to talk...")

    audio = microphone.record()

    text = recognizer.transcribe(audio)

    print()
    print("Recognized:")
    print(text)

    detected, command_text = detector.detect(text)

    if not detected:

        print()
        print("Wake phrase not detected.")
        continue

    print()
    print("Command:")
    print(command_text)

    command = parser.parse(command_text)

    if command is None:

        print()
        print("Couldn't understand command.")
        continue

    response = engine.process(command)

    print()
    print(f"🤖 {response.message}")