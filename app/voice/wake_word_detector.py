import string

from app.voice.wake_word import WAKE_PHRASES


class WakeWordDetector:

    def detect(self, text: str):

        # Normalize
        text = text.lower().strip()

        # Remove punctuation
        text = text.translate(
            str.maketrans("", "", string.punctuation)
        )

        # Check every wake phrase
        for phrase in WAKE_PHRASES:

            if text.startswith(phrase):

                command = text[len(phrase):].strip()

                return True, command

        return False, text