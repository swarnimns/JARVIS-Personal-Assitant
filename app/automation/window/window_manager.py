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

            # Get the window title
            title = win32gui.GetWindowText(hwnd)

            # Ignore helper windows with no title
            if not title.strip():
                return True

            # Ignore the Windows desktop
            if title == "Program Manager":
                return True


            # Some windows disappear while we're enumerating them
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
            except Exception:
                return True

            # Some processes may disappear before we can inspect them
            try:
                process_name = psutil.Process(pid).name()

                title = win32gui.GetWindowText(hwnd)

                if "steam" in title.lower():                  
                    print(f"TITLE: {title}")
                    print(f"PROCESS: {process_name}")
                    print(f"PID: {pid}")
                    print("-" * 40)

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                return True

            # Is this the application we're looking for?
            if process_name.lower() == application.window_process.lower():

                print(f"Matched window: '{title}' ({process_name})")

                # We found the correct window.
                # Even if Windows refuses to focus it,
                # we still consider it found.
                found = True

                try:
                    # Restore if minimized
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

                    # Bring to front
                    win32gui.SetForegroundWindow(hwnd)

                except Exception as e:
                    print(f"Window Error: {e}")

                # Stop searching after the first valid window
                return False

            return True

        try:
            win32gui.EnumWindows(callback, None)
        except Exception as e:
            print(f"EnumWindows Error: {e}")

        print("Returning:", found)

        return found