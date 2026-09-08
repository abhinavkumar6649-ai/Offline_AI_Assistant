
from modules.wakeword import wait_for_wake_word

if __name__ == "__main__":
    print("Testing Wake Word Detection...")
    print("Please say 'Hey Jarvis' into your microphone...")

    wait_for_wake_word()

    print("🚀 Jarvis activated!")

