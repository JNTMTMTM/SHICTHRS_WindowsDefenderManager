# SHICTHRS Windows Defender Manager

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)

一个用于管理Windows Defender的Python工具，提供简单易用的API来启用、禁用和检查Windows Defender状态。

## 功能特点

- 检查Windows Defender的当前状态
- 启用Windows Defender
- 禁用Windows Defender
- 简洁易用的Python API
- 详细的错误处理和异常信息

## 安装

### 依赖要求

- Python 3.x
- Windows 操作系统
- 管理员权限（用于修改Windows Defender设置）

### 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/JNTMTMTM/SHICTHRS_WindowsDefenderManager.git
```

2. 安装依赖：
```bash
pip install -r requirement.txt
```

3. 确保以管理员身份运行您的Python脚本或命令提示符

## 使用方法

### 基本用法

```python
from SHICTHRSWindowsDefenderManager.SHICTHRSWindowsDefenderManager import *

# 检查Windows Defender状态
is_enabled = SHRWindowsDefenderManager_check_defender()
print(f"Windows Defender 启用状态: {is_enabled}")

# 禁用Windows Defender
SHRWindowsDefenderManager_disable_defender()

# 启用Windows Defender
SHRWindowsDefenderManager_enable_defender()
```

### 示例脚本

```python
from SHICTHRSWindowsDefenderManager.SHICTHRSWindowsDefenderManager import *

try:
    # 检查当前状态
    status = SHRWindowsDefenderManager_check_defender()
    print(f"当前Windows Defender状态: {'启用' if status else '禁用'}")
    
    # 切换状态
    if status:
        print("正在禁用Windows Defender...")
        SHRWindowsDefenderManager_disable_defender()
        print("Windows Defender已禁用")
    else:
        print("正在启用Windows Defender...")
        SHRWindowsDefenderManager_enable_defender()
        print("Windows Defender已启用")
    
    # 验证更改
    new_status = SHRWindowsDefenderManager_check_defender()
    print(f"新状态: {'启用' if new_status else '禁用'}")
    
except SHRWindowsDefenderManagerException as e:
    print(f"错误: {e}")
```

## API 参考

### `SHRWindowsDefenderManager_check_defender() -> bool`
检查Windows Defender的当前状态。

**返回值:**
- `True`: Windows Defender 已启用
- `False`: Windows Defender 已禁用

### `SHRWindowsDefenderManager_enable_defender() -> None`
启用Windows Defender。

**可能抛出:**
- `SHRWindowsDefenderManagerException`: 启用失败时抛出

### `SHRWindowsDefenderManager_disable_defender() -> None`
禁用Windows Defender。

**可能抛出:**
- `SHRWindowsDefenderManagerException`: 禁用失败时抛出

### `SHRWindowsDefenderManagerException`
自定义异常类，用于处理Windows Defender管理过程中的错误。

## 注意事项

- 本工具需要管理员权限才能正常工作
- 修改Windows Defender设置可能会影响系统安全性，请谨慎使用
- 建议在禁用Windows Defender前确保有其他安全措施
- 本工具仅适用于Windows系统

## 许可证

本项目采用 GPL-3.0 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 作者

SHICTHRS-JNTMTMTM

## 版权

Copyright © 2025-2026 SHICTHRS, Std. All rights reserved.

## 支持

如果您遇到任何问题或有任何建议，请在GitHub上创建一个issue。