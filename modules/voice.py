import os
import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000
DURATION = 5

def record_audio(filename="recordings/input.wav"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    print("🎤 Speak now...")

    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    sf.write(filename, audio, SAMPLE_RATE)

    print("✅ Recording Saved")

if __name__ == "__main__":
    record_audio()