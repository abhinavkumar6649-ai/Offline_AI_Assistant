import subprocess


def speak(text: str):
    """
    Convert text to speech using macOS built-in 'say' command.
    """
    subprocess.run(["say", text])
