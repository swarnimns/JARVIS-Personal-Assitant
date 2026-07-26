import string

from app.voice.wake_word import WAKE_PHRASES


class WakeWordDetector:

    def detect(self, text: str):

        text = text.lower().strip()

        for phrase in WAKE_PHRASES:

            if text.startswith(phrase):

                command = text[len(phrase):].strip()

                command = command.lstrip(string.punctuation + " ")

                return True, command

        return False, text