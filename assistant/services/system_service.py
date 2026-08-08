"""
=========================================
AMNA AI Assistant
System Service
=========================================
"""

import webbrowser

from assistant.automation import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode,
    open_pycharm,
    open_cmd,
    open_powershell,
    open_file_explorer,
    open_downloads,
    open_documents,
    open_desktop,
    shutdown_pc,
    restart_pc,
    cancel_shutdown,
    lock_pc,
)


class SystemService:

    # ==========================================
    # Applications
    # ==========================================

    def open_notepad(self):
        return open_notepad()

    def open_calculator(self):
        return open_calculator()

    def open_chrome(self):
        return open_chrome()

    def open_vscode(self):
        return open_vscode()

    def open_pycharm(self):
        return open_pycharm()

    def open_cmd(self):
        return open_cmd()

    def open_powershell(self):
        return open_powershell()

    def open_file_explorer(self):
        return open_file_explorer()

    # ==========================================
    # Folders
    # ==========================================

    def open_downloads(self):
        return open_downloads()

    def open_documents(self):
        return open_documents()

    def open_desktop(self):
        return open_desktop()

    # ==========================================
    # Websites
    # ==========================================

    def open_google(self):
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    def open_github(self):
        webbrowser.open("https://github.com")
        return "Opening GitHub."

    def open_chatgpt(self):
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT."

    # ==========================================
    # System
    # ==========================================

    def shutdown(self):
        return shutdown_pc()

    def restart(self):
        return restart_pc()

    def cancel_shutdown(self):
        return cancel_shutdown()

    def lock(self):
        return lock_pc()