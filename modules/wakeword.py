import os
import numpy as np
import sounddevice as sd
from openwakeword.model import Model

SAMPLE_RATE = 16000
CHUNK_SIZE = 1280

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    ".venv",
    "lib",
    "python3.13",
    "site-packages",
    "openwakeword",
    "resources",
    "models",
    "hey_jarvis_v0.1.onnx"
)

MODEL_PATH = os.path.abspath(MODEL_PATH)


def wait_for_wake_word():
    print("🎤 Listening for wake word: 'Hey Jarvis'...")
    print("Say 'Hey Jarvis'...")

    model = Model(
        wakeword_models=[MODEL_PATH],
        inference_framework="onnx"
    )

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        blocksize=CHUNK_SIZE
    ) as stream:

        while True:
            audio, overflowed = stream.read(CHUNK_SIZE)

            audio = np.squeeze(audio)

            prediction = model.predict(audio)

            for name, score in prediction.items():
                print(f"\r{name}: {score:.3f}", end="")

                if score > 0.5:
                    print("\n\n✅ Hey Jarvis detected!")
                    return True
