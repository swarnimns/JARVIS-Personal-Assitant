import psutil

from app.models.application import Application

class ProcessManager:

    def find_running_process(self, application: Application):

        # Ask Windows for all running processes
        processes = psutil.process_iter()

        # Loop through every process
        for process in processes:

            if process.name() == application.process:

                #
                print(
                    f"PID: {process.pid} | "
                    f"Name: {process.name()} | "
                    f"Exe: {process.exe()}"
                )

                return process

        return None

        # Compare the process name

        # If found, return the process

        # Otherwise return None