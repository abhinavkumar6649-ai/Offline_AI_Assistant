import subprocess
import webbrowser
from datetime import datetime


def open_website(url):
    webbrowser.open(url)
    return f"Opening {url}"


def open_app(app_name):
    try:
        subprocess.Popen(["open", "-a", app_name])
        return f"Opening {app_name}"
    except Exception:
        return f"I could not open {app_name}"


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%A, %d %B %Y")
