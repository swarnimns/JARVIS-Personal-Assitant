import subprocess

from app.config.app_registry import APPLICATIONS


class DesktopHandler:

    def open_application(self, app_name: str):

        app = APPLICATIONS.get(app_name.lower())

        if app is None:
            print(f"{app_name} is not registered.")
            return

        try:

            subprocess.Popen(app)

            print(f"Opening {app_name}...")

        except Exception as e:

            print(f"Error: {e}")