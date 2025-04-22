import sys
import os
import builtins
_original_sys_exit = sys.exit
_original_os_exit = os._exit

def patch_exit():
    # Patch commonly-used exit functions
    sys.exit = _original_sys_exit
    builtins.exit = _original_sys_exit
    builtins.quit = _original_sys_exit
    os._exit = _original_os_exit  # Optional, use carefully


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
