from modules.memory import create_database, save_memory, get_memory
from modules.speaker import speak
from modules.voice import record_audio
from modules.stt import speech_to_text
from modules.brain import ask_ai
from modules.wakeword import wait_for_wake_word


print("=" * 60)
print("🤖 Project Jarvis Voice Assistant")
print("=" * 60)

create_database()

print("\n🟢 Jarvis is ready!")
print("Say 'Hey Jarvis' to activate.")


while True:

    # Wake Word
    wait_for_wake_word()

    print("\n🔔 Jarvis activated!")
    speak("Yes?")

    # Continuous Conversation
    while True:

        print("\n🎤 Listening for your command...")
        record_audio()

        # Speech to Text
        user_text = speech_to_text("recordings/input.wav").strip()

        if not user_text:
            print("⚠️ I didn't hear anything.")
            continue

        print("\n🧑 You:", user_text)

        command = user_text.lower()

        # Exit completely
        if command in ["exit", "quit", "bye", "shutdown jarvis"]:
            print("👋 Goodbye!")
            speak("Goodbye!")
            exit()

        # End conversation and return to wake word
        if command in [
            "stop",
            "stop listening",
            "go to sleep",
            "sleep jarvis"
        ]:
            print("😴 Going back to sleep...")
            speak("Okay, I am going to sleep.")
            break

        # Save Name
        if command.startswith("my name is "):
            name = user_text[11:].strip()

            save_memory("name", name)

            response = f"Nice to meet you, {name}. I will remember your name."

            print("\n🤖 Jarvis:")
            print(response)

            speak(response)
            continue

        # Recall Name
        if "what is my name" in command:
            name = get_memory("name")

            if name:
                response = f"Your name is {name}."
            else:
                response = "I don't know your name yet."

            print("\n🤖 Jarvis:")
            print(response)

            speak(response)
            continue

        # Normal AI Chat
        response = ask_ai(user_text)

        print("\n🤖 Jarvis:")
        print(response)

        speak(response)
