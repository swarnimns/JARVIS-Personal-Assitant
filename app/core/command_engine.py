from app.automation.browser.browser_handler import BrowserHandler
from app.core.command import Command
from app.automation.desktop.desktop_handler import DesktopHandler
from app.responses.response import Response



class CommandEngine:

    def __init__(self):

        self.desktop = DesktopHandler()

        self.browser = BrowserHandler()


    def process(self, command: Command):

        print("=" * 40)
        print("JARVIS COMMAND ENGINE")
        print("=" * 40)

        print(f"Action : {command.action}")
        print(f"Target : {command.target}")
        print(f"Source : {command.source}")

        print()

        if command.action == "open":

            # First try opening as a desktop application
            response = self.desktop.open_application(command.target)

            if response.success:
                return response

            # If not found, try opening as a website
            response = self.browser.open_website(command.target)

            return response

        elif command.action == "search":
            response = self.browser.search(
                command.target,
                command.query
            )

            return response
        

        elif command.action == "close":
            response = self.desktop.close_application(command.target)
            return response

        else:
            return Response(
                success=False,
                message=f"Unknown action: {command.action}"
            )