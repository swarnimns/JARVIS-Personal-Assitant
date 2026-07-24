import psutil

from app.models.application import Application


class ProcessManager:

    def find_running_process(self, application: Application):

        for process in psutil.process_iter(["pid", "name"]):

            try:

                process_name = process.info["name"]

                if (
                    process_name
                    and process_name.lower() == application.process.lower()
                ):

                    print(
                        f"PID: {process.pid} | "
                        f"Name: {process_name}"
                    )

                    return process

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                continue

        return None