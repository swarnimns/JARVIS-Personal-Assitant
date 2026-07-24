import psutil
import win32con
import win32gui
import win32process


class WindowManager:
    """
    Handles application windows.

    Responsibilities:
    - Find visible application windows
    - Ignore helper/hidden windows
    - Restore minimized windows
    - Bring existing windows to the foreground
    """

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

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                return True

            # ---------------------------------------------------------
            # DEBUGGING
            #
            # Uncomment when debugging applications that don't
            # come to the front correctly.
            #
            # if "steam" in title.lower():
            #     print(f"TITLE: {title}")
            #     print(f"PROCESS: {process_name}")
            #     print(f"PID: {pid}")
            #     print("-" * 40)
            #
            # Replace "steam" with:
            #   calculator
            #   spotify
            #   discord
            #   chrome
            # etc.
            # ---------------------------------------------------------

            # Is this the application's window?
            if process_name.lower() == application.window_process.lower():

                # Uncomment for debugging
                # print(f"Matched window: '{title}' ({process_name})")

                found = True

                try:
                    # Restore if minimized
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

                    # Bring to front
                    win32gui.SetForegroundWindow(hwnd)

                except Exception:
                    # Windows occasionally refuses to focus
                    # even though we found the correct window.
                    pass

                # Stop searching after the first match
                return False

            return True

        try:
            win32gui.EnumWindows(callback, None)
        except Exception:
            # Ignore transient Win32 enumeration errors
            pass

        # Uncomment for debugging
        # print("Returning:", found)

        return found