from app.automation.process.process_manager import ProcessManager
from app.config.app_registry import find_application

manager = ProcessManager()

chrome = find_application("chrome")

process = manager.find_running_process(chrome)

print(process)