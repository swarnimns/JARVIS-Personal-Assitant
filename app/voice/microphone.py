import time

import sounddevice as sd
from scipy.io.wavfile import write


class Microphone:

    def __init__(self):

        self.sample_rate = 16000
        self.channels = 1

    def record(self, duration=5, filename="recording.wav"):

        print()
        print("🎤 Get ready...")

        # Give yourself half a second before recording starts
        time.sleep(0.5)

        print("🎙️ Recording...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16"
        )

        sd.wait()

        # Small pause after speaking
        time.sleep(0.5)

        write(filename, self.sample_rate, audio)

        print(f"✅ Saved recording to {filename}")

        return filename