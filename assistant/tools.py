import os
import subprocess
import webbrowser
from datetime import datetime
import socket

# ==========================================================
# IDENTITY
# ==========================================================

def who_are_you():
    return "I am AMNA, your personal AI assistant, created and developed by Amit Yadav."


def who_created_you():
    return "I was created and developed by Amit Yadav."


def who_is_your_owner():
    return "My owner and developer is Amit Yadav."


def tell_about_amna():
    return (
        "I am AMNA, an intelligent personal AI assistant built by "
        "Amit Yadav. I can help with coding, AI, SAP, automation, "
        "web browsing, productivity, and much more."
    )


# ==========================================================
# APPLICATIONS
# ==========================================================

def open_notepad():
    os.system("notepad")
    return "Opening Notepad."


def open_calculator():
    os.system("calc")
    return "Opening Calculator."


def open_cmd():
    os.system("start cmd")
    return "Opening Command Prompt."


def open_powershell():
    os.system("start powershell")
    return "Opening PowerShell."


def open_file_explorer():
    os.system("explorer")
    return "Opening File Explorer."


def open_chrome():
    try:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
    except:
        webbrowser.open("https://www.google.com")

    return "Opening Chrome."


def open_vscode():
    try:
        subprocess.Popen(["code"])
        return "Opening VS Code."
    except:
        return "VS Code is not installed or 'code' is not added to PATH."


def open_pycharm():
    possible_paths = [
        r"C:\Program Files\JetBrains\PyCharm Community Edition 2025.2\bin\pycharm64.exe",
        r"C:\Program Files\JetBrains\PyCharm Community Edition 2025.1\bin\pycharm64.exe",
        r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.3\bin\pycharm64.exe",
        r"C:\Program Files\JetBrains\PyCharm Professional Edition 2025.2\bin\pycharm64.exe",
    ]

    for path in possible_paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return "Opening PyCharm."

    return "PyCharm executable not found. Update its path in tools.py."


# ==========================================================
# DATE & TIME
# ==========================================================

def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%d-%m-%Y")


# ==========================================================
# WEB
# ==========================================================

def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google."


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube."


def open_github():
    webbrowser.open("https://github.com")
    return "Opening GitHub."


def open_chatgpt():
    webbrowser.open("https://chatgpt.com")
    return "Opening ChatGPT."


def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")
    return f"Searching Google for '{query}'."


def search_youtube(query):
    webbrowser.open(
        f"https://www.youtube.com/results?search_query={query}"
    )
    return f"Searching YouTube for '{query}'."


# ==========================================================
# FOLDERS
# ==========================================================

def open_downloads():
    os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
    return "Opening Downloads."


def open_documents():
    os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
    return "Opening Documents."


def open_desktop():
    os.startfile(os.path.join(os.path.expanduser("~"), "Desktop"))
    return "Opening Desktop."


# ==========================================================
# SYSTEM
# ==========================================================

def shutdown_pc():
    os.system("shutdown /s /t 10")
    return "Your PC will shut down in 10 seconds."


def restart_pc():
    os.system("shutdown /r /t 10")
    return "Your PC will restart in 10 seconds."


def cancel_shutdown():
    os.system("shutdown /a")
    return "Shutdown or restart cancelled."


def lock_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "Locking your computer."


# ==========================================================
# NETWORK
# ==========================================================

def get_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip