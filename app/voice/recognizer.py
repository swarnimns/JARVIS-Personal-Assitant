from faster_whisper import WhisperModel


class SpeechRecognizer:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )

        print("Whisper model loaded.")

    def transcribe(self, audio_file: str):

        segments, info = self.model.transcribe(
            audio_file,
            language="en",
            beam_size=5,
            vad_filter=True
        )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return text.strip()