import psutil
import win32con
import win32gui
import win32process


class WindowManager:

    def bring_to_front(self, application):

        found = False

        def callback(hwnd, extra):

            nonlocal found

            # Ignore invisible windows
            if not win32gui.IsWindowVisible(hwnd):
                return True

            # Some windows disappear while we're enumerating them
            try:
                thread_id, pid = win32process.GetWindowThreadProcessId(hwnd)
            except Exception:
                return True

            # Some processes may disappear before we can inspect them
            try:
                process_name = psutil.Process(pid).name()
            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess
            ):
                return True

            # Is this the application we're looking for?
            if process_name.lower() == application.process.lower():

                try:
                    # Restore if minimized
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

                    # Bring to front
                    win32gui.SetForegroundWindow(hwnd)

                    found = True

                except Exception as e:
                    print(f"Window Error: {e}")

                # Stop searching
                return False

            return True

        try:
            win32gui.EnumWindows(callback, None)
        except Exception as e:
            print(f"EnumWindows Error: {e}")

        return found