
import winreg

WINDOWS_DEFENDER_KEY_PATH = r"SOFTWARE\Policies\Microsoft\Windows Defender"
REAL_TIME_PROTECTION_KEY_PATH = r"SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection"

def enable_defender(error_class) -> None:
    try:
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE , WINDOWS_DEFENDER_KEY_PATH)
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE , REAL_TIME_PROTECTION_KEY_PATH)
    except PermissionError as e:
        raise error_class(f"SHRWindowsDefenderManager [ERROR.4001.0] unable to enable Windows Defender due to PermissionError | {str(e)}")
