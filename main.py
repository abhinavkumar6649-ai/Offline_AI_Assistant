from modules.memory import create_database, save_memory, get_memory
from modules.speaker import speak
from modules.voice import record_audio
from modules.stt import speech_to_text
from modules.brain import ask_ai

print("=" * 60)
print("🤖 Project Jarvis Voice Assistant")
print("=" * 60)

# Create database if it doesn't exist
create_database()

while True:
    input("\nPress ENTER to Speak...")

    # Record voice
    record_audio()

    # Convert speech to text
    user_text = speech_to_text("recordings/input.wav").strip()

    print("\n🧑 You:", user_text)

    # Exit command
    if user_text.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye!")
        speak("Goodbye!")
        break

    # ---------------- Memory: Save Name ----------------
    if user_text.lower().startswith("my name is "):
        name = user_text[11:].strip()

        save_memory("name", name)

        response = f"Nice to meet you, {name}. I will remember your name."

        print("\n🤖 Jarvis:")
        print(response)

        speak(response)
        continue

    # ---------------- Memory: Recall Name ----------------
    if "what is my name" in user_text.lower():
        name = get_memory("name")

        if name:
            response = f"Your name is {name}."
        else:
            response = "I don't know your name yet."

        print("\n🤖 Jarvis:")
        print(response)

        speak(response)
        continue

    # ---------------- Normal AI Chat ----------------
    response = ask_ai(user_text)

    print("\n🤖 Jarvis:")
    print(response)

    speak(response)