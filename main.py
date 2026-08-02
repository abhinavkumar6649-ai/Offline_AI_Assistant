from modules.voice import record_audio
from modules.stt import speech_to_text
from modules.brain import ask_ai

print("=" * 60)
print("🤖 Project Jarvis Voice Assistant")
print("=" * 60)

while True:
    input("\nPress ENTER to Speak...")

    record_audio()

    user_text = speech_to_text("recordings/input.wav")

    print("\n🧑 You:", user_text)

    if user_text.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye!")
        break

    response = ask_ai(user_text)

    print("\n🤖 Jarvis:\n")
    print(response)