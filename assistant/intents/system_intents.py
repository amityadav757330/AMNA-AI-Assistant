from assistant.tools import *


class SystemIntent:

    def handle(self, command):

        command = command.lower().strip()

        commands = {

            # Applications
            "open notepad": open_notepad,
            "open calculator": open_calculator,
            "open chrome": open_chrome,
            "open vscode": open_vscode,
            "open vs code": open_vscode,
            "open pycharm": open_pycharm,
            "open command prompt": open_cmd,
            "open cmd": open_cmd,
            "open powershell": open_powershell,
            "open file explorer": open_file_explorer,

            # Folders
            "open downloads": open_downloads,
            "open documents": open_documents,
            "open desktop": open_desktop,

            # Websites
            "open google": open_google,
            "open youtube": open_youtube,
            "open github": open_github,
            "open chatgpt": open_chatgpt,

            # System
            "shutdown": shutdown_pc,
            "restart": restart_pc,
            "cancel shutdown": cancel_shutdown,
            "lock pc": lock_pc,
        }

        for keyword, function in commands.items():

            if keyword in command:
                return function()

        return None