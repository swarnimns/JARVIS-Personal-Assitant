from app.voice.wake_word_detector import WakeWordDetector

detector = WakeWordDetector()

while True:

    text = input("Speech: ")

    detected, command = detector.detect(text)

    print("Detected :", detected)
    print("Command  :", command)
    print()