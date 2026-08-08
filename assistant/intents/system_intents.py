"""
=========================================
AMNA AI Assistant
System Intent Handler
=========================================
"""

from assistant.services.system_service import SystemService


class SystemIntent:

    def __init__(self):

        self.system = SystemService()

    # ==========================================
    # Handle System Command
    # ==========================================

    def handle(self, command):

        if not command:
            return None

        command = command.lower().strip()

        commands = {

            # ==========================================
            # Applications
            # ==========================================

            "open notepad": self.system.open_notepad,

            "open calculator": self.system.open_calculator,

            "open chrome": self.system.open_chrome,

            "open vscode": self.system.open_vscode,

            "open vs code": self.system.open_vscode,

            "open pycharm": self.system.open_pycharm,

            "open command prompt": self.system.open_cmd,

            "open cmd": self.system.open_cmd,

            "open powershell": self.system.open_powershell,

            "open file explorer": self.system.open_file_explorer,

            # ==========================================
            # Folders
            # ==========================================

            "open downloads": self.system.open_downloads,

            "open documents": self.system.open_documents,

            "open desktop": self.system.open_desktop,

            # ==========================================
            # Websites
            # ==========================================

            "open google": self.system.open_google,

            "open youtube": self.system.open_youtube,

            "open github": self.system.open_github,

            "open chatgpt": self.system.open_chatgpt,

            # ==========================================
            # System
            # ==========================================

            "shutdown": self.system.shutdown,

            "restart": self.system.restart,

            "cancel shutdown": self.system.cancel_shutdown,

            "lock pc": self.system.lock,
        }

        # ==========================================
        # Find Command
        # ==========================================

        for keyword, function in commands.items():

            if keyword in command:

                try:

                    return function()

                except Exception as error:

                    print(
                        f"[SystemIntent Error] "
                        f"{keyword}: {error}"
                    )

                    return None

        return None