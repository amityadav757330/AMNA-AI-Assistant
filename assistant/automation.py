"""
=========================================
AMNA AI Assistant
Automation Layer
=========================================
"""

import os
import subprocess
import webbrowser


# ==========================================
# Applications
# ==========================================

def open_notepad():

    subprocess.Popen(["notepad.exe"])

    return "Opening Notepad."


def open_calculator():

    subprocess.Popen(["calc.exe"])

    return "Opening Calculator."


def open_chrome():

    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for path in chrome_paths:

        if os.path.exists(path):

            subprocess.Popen([path])

            return "Opening Chrome."

    webbrowser.open("https://www.google.com")

    return "Opening Chrome."


def open_vscode():

    try:

        subprocess.Popen(["code"])

        return "Opening Visual Studio Code."

    except FileNotFoundError:

        return "Visual Studio Code was not found."


def open_pycharm():

    try:

        subprocess.Popen(["pycharm"])

        return "Opening PyCharm."

    except FileNotFoundError:

        return "PyCharm was not found."


def open_cmd():

    subprocess.Popen(["cmd.exe"])

    return "Opening Command Prompt."


def open_powershell():

    subprocess.Popen(["powershell.exe"])

    return "Opening PowerShell."


def open_file_explorer():

    subprocess.Popen(["explorer.exe"])

    return "Opening File Explorer."


# ==========================================
# Folders
# ==========================================

def open_downloads():

    path = os.path.join(
        os.path.expanduser("~"),
        "Downloads"
    )

    os.startfile(path)

    return "Opening Downloads."


def open_documents():

    path = os.path.join(
        os.path.expanduser("~"),
        "Documents"
    )

    os.startfile(path)

    return "Opening Documents."


def open_desktop():

    path = os.path.join(
        os.path.expanduser("~"),
        "Desktop"
    )

    os.startfile(path)

    return "Opening Desktop."


# ==========================================
# Websites
# ==========================================

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


# ==========================================
# System
# ==========================================

def shutdown_pc():

    os.system("shutdown /s /t 5")

    return "Shutting down the computer."


def restart_pc():

    os.system("shutdown /r /t 5")

    return "Restarting the computer."


def cancel_shutdown():

    os.system("shutdown /a")

    return "Shutdown cancelled."


def lock_pc():

    os.system("rundll32.exe user32.dll,LockWorkStation")

    return "Locking the computer."