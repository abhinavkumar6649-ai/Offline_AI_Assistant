import ssl
import soundfile as sf
import whisper

# Bypass SSL certificate verification for downloading model weights on macOS
ssl._create_default_https_context = ssl._create_unverified_context

print("🧠 Loading Whisper model... (First time may take a few seconds)")

model = whisper.load_model("base")


def speech_to_text(audio_file: str) -> str:
    # Load audio array directly with soundfile to avoid ffmpeg system dependency
    audio_data, sample_rate = sf.read(audio_file, dtype="float32")
    if audio_data.ndim > 1:
        audio_data = audio_data.mean(axis=1)

    result = model.transcribe(audio_data, fp16=False)
    return result["text"].strip()


if __name__ == "__main__":
    text = speech_to_text("recordings/input.wav")

    print("\nRecognized Text:")
    print(text)