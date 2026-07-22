from app.core.command import Command
from app.automation.desktop.desktop_handler import DesktopHandler


class CommandEngine:

    def __init__(self):

        self.desktop = DesktopHandler()

    def process(self, command: Command):

        print("=" * 40)
        print("JARVIS COMMAND ENGINE")
        print("=" * 40)

        print(f"Action : {command.action}")
        print(f"Target : {command.target}")
        print(f"Source : {command.source}")

        print()

        if command.action == "open":

            self.desktop.open_application(command.target)

        else:

            print("Unknown command.")