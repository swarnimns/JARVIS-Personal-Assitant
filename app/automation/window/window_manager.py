import psutil
import win32con
import win32gui
import win32process


class WindowManager:
    """
    Handles application windows.

    Responsibilities:
    - Find visible application windows
    - Bring windows to the foreground
    - Close windows gracefully
    """

    def bring_to_front(self, application):

        found = False

        def callback(hwnd, extra):

            nonlocal found

            # Ignore invisible windows
            if not win32gui.IsWindowVisible(hwnd):
                return True

            # Window title
            title = win32gui.GetWindowText(hwnd)

            # Ignore helper windows
            if not title.strip():
                return True

            # Ignore the desktop
            if title == "Program Manager":
                return True

            # Get the window's process ID
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
            except Exception:
                return True

            # Get the process name
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
            # Uncomment when debugging a specific application.
            #
            # if "steam" in title.lower():
            #     print(f"TITLE: {title}")
            #     print(f"PROCESS: {process_name}")
            #     print(f"PID: {pid}")
            #     print("-" * 40)
            #
            # ---------------------------------------------------------

            # Is this our application's window?
            if process_name.lower() == application.window_process.lower():

                found = True

                try:
                    # Restore if minimized
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

                    # Bring to front
                    win32gui.SetForegroundWindow(hwnd)

                except Exception:
                    pass

                # Stop searching
                return False

            return True

        try:
            win32gui.EnumWindows(callback, None)
        except Exception:
            pass

        return found


    def close_window(self, application):

        found = False

        def callback(hwnd, extra):

            nonlocal found

            # Ignore invisible windows
            if not win32gui.IsWindowVisible(hwnd):
                return True

            # Window title
            title = win32gui.GetWindowText(hwnd)

            # Ignore helper windows
            if not title.strip():
                return True

            # Ignore the desktop
            if title == "Program Manager":
                return True

            # Get the window's process ID
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
            except Exception:
                return True

            # Get the process name
            try:
                process_name = psutil.Process(pid).name()

            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                return True

            # Is this our application's window?
            if process_name.lower() == application.window_process.lower():

                found = True

                try:
                    #Open it if you want to Debug.
                    #print(f"Closing window: {title}")
                    #print(f"HWND: {hwnd}")
                    #print(f"PROCESS: {process_name}")

                    # Politely ask Windows to close the window
                    win32gui.PostMessage(
                        hwnd,
                        win32con.WM_SYSCOMMAND,
                        win32con.SC_CLOSE,
                        0
                    )

                except Exception as e:
                    print(e)

                # Stop searching
                return False

            return True

        try:
            win32gui.EnumWindows(callback, None)
        except Exception:
            pass

        return found