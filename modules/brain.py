import ollama

from modules.memory import (
    save_conversation,
    get_conversation,
    clear_conversation as clear_saved_conversation
)

MODEL_NAME = "gemma3:4b"

MAX_HISTORY = 10


def ask_ai(prompt: str) -> str:

    # Save user message
    save_conversation("user", prompt)

    # Load recent conversation from SQLite
    conversation_history = get_conversation(MAX_HISTORY)

    response = ollama.chat(
        model=MODEL_NAME,
        messages=conversation_history
    )

    answer = response.message.content

    # Save Jarvis response
    save_conversation("assistant", answer)

    return answer


def clear_conversation():

    clear_saved_conversation()
