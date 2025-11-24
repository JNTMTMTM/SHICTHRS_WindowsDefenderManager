
import winreg

WINDOWS_DEFENDER_KEY_PATH = r"SOFTWARE\Policies\Microsoft\Windows Defender"

def check_defender() -> bool:
    try:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE , WINDOWS_DEFENDER_KEY_PATH) as key:
                try:
                    value , reg_type = winreg.QueryValueEx(key, "DisableAntiSpyware")
                    if value == 1:
                        return False
                except FileNotFoundError:
                    pass
        except FileNotFoundError:
            pass
        
        rt_key_path = WINDOWS_DEFENDER_KEY_PATH + r"\Real-Time Protection"
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE , rt_key_path) as rt_key:
                disabled_features = []
                
                for feature in ["DisableRealtimeMonitoring" , "DisableBehaviorMonitoring" , "DisableIOAVProtection"]:
                    try:
                        value , reg_type = winreg.QueryValueEx(rt_key, feature)
                        if value == 1:
                            disabled_features.append(feature)
                    except FileNotFoundError:
                        pass
                
                if disabled_features:
                    return True

        except FileNotFoundError:
            pass
        
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE , r"SYSTEM\CurrentControlSet\Services\WinDefend") as svc_key:
                try:
                    start_value , reg_type = winreg.QueryValueEx(svc_key, "Start")
                    if start_value == 4:
                        return False
                except FileNotFoundError:
                    pass
        except FileNotFoundError:
            pass
        
        return True
    
    except:
        return False
