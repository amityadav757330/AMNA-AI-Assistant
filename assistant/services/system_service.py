import webbrowser

from assistant.automation import (
    open_notepad,
    open_calculator,
    open_chrome,
    open_vscode,
    open_pycharm,
    open_downloads,
    open_documents,
    open_desktop,
    shutdown_pc,
    restart_pc,
    cancel_shutdown,
    lock_pc,
)


class SystemService:

    # -------------------------
    # Applications
    # -------------------------

    def open_notepad(self):
        open_notepad()

    def open_calculator(self):
        open_calculator()

    def open_chrome(self):
        open_chrome()

    def open_vscode(self):
        open_vscode()

    def open_pycharm(self):
        open_pycharm()

    # -------------------------
    # Folders
    # -------------------------

    def open_downloads(self):
        open_downloads()

    def open_documents(self):
        open_documents()

    def open_desktop(self):
        open_desktop()

    # -------------------------
    # Websites
    # -------------------------

    def open_google(self):
        webbrowser.open("https://www.google.com")

    def open_youtube(self):
        webbrowser.open("https://www.youtube.com")

    def open_github(self):
        webbrowser.open("https://github.com")

    def open_chatgpt(self):
        webbrowser.open("https://chat.openai.com")

    # -------------------------
    # System
    # -------------------------

    def shutdown(self):
        shutdown_pc()

    def restart(self):
        restart_pc()

    def cancel_shutdown(self):
        cancel_shutdown()

    def lock(self):
        lock_pc()