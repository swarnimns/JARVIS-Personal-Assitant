import subprocess

from app.config.app_registry import find_application
from app.responses.response import Response

class DesktopHandler:

    def open_application(self, app_name: str):

        app = find_application(app_name.lower())

        if app is None:
        
                return Response(
                    success=False,
                    message=f"{app_name} is not registered."
                )

        try:

             subprocess.Popen(app.path)

             return Response(
                  success=True,
                  message=f"Opening {app.name}..."
             )

        except Exception as e:

             return Response(
                  success=False,
                  message=f"Error: {e}"
             )
        
           



   

    