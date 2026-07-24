import subprocess

from app.automation.process.process_manager import ProcessManager
from app.config.app_registry import find_application
from app.responses.response import Response
from app.automation.window.window_manager import WindowManager


class DesktopHandler:

    def __init__(self):

        self.process_manager = ProcessManager()
        self.window_manager = WindowManager()

    def open_application(self, app_name: str):

        # Find the application in the registry
        app = find_application(app_name.lower())

        # Application not found
        if app is None:

            return Response(
                success=False,
                message=f"{app_name} is not registered."
            )

        # Check if it is already running
        running_process = self.process_manager.find_running_process(app)

        if running_process:

            focused = self.window_manager.bring_to_front(app)

            if focused:
                return Response(
                success=True,
                message=f"Bringing {app.name} to the front..."
                )

        # Process exists, but no visible window.
        # Launch the application.
            subprocess.Popen(app.path)

            return Response(
            success=True,
            message=f"Opening {app.name}..."
            )

        # Application isn't running at all.
        subprocess.Popen(app.path)

        return Response(
            success=True,
            message=f"Opening {app.name}..."
        )
