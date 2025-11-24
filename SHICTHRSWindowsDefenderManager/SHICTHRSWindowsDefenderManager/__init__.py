# *-* coding: utf-8 *-*
# src\__init__.py
# SHICTHRS Windows Defender Manager
# AUTHOR : SHICTHRS-JNTMTMTM
# Copyright : © 2025-2026 SHICTHRS, Std. All rights reserved.
# lICENSE : GPL-3.0

import os
from colorama import init
init()

from .utils.SHRWindowsDefenderManager_check_defender import check_defender
from .utils.SHRWindowsDefenderManager_enable_defender import enable_defender

print('\033[1mWelcome to use SHRWindowsDefenderManager - enable/disable Windows Defender\033[0m\n|  \033[1;34mGithub : https://github.com/JNTMTMTM/SHICTHRS_WindowsDefenderManager\033[0m')
print('|  \033[1mAlgorithms = rule ; Questioning = approval\033[0m')
print('|  \033[1mCopyright : © 2025-2026 SHICTHRS, Std. All rights reserved.\033[0m\n')

class SHRWindowsDefenderManagerException(BaseException):
    def __init__(self , message: str) -> None:
        self.message = message
    
    def __str__(self):
        return self.message

def SHRWindowsDefenderManager_check_defender() -> bool:
    try:
        return check_defender()
    except Exception as e:
        raise SHRWindowsDefenderManagerException(f"SHRWindowsDefenderManager [ERROR.4000] unable to check Windows Defender status. | {str(e)}")

def SHRWindowsDefenderManager_enable_defender() -> None:
    try:
        enable_defender(SHRWindowsDefenderManagerException)
        if not SHRWindowsDefenderManager_check_defender():
            raise SHRWindowsDefenderManagerException(f"SHRWindowsDefenderManager [ERROR.4001.1] failed to enable Windows Defender.")
    except Exception as e: 
        raise SHRWindowsDefenderManagerException(f"SHRWindowsDefenderManager [ERROR.4001] unable to enable Windows Defender. | {str(e)}")