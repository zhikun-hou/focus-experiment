import sys
import os
# 必须在整个实验脚本的最前面from loader import *，否则无法实现屏蔽pygame输出的效果

# ==========屏蔽模块==========

# 把stdout重定向到一个空的管道中，避免pygame的输出对Electron-Python的管道造成影响
sys.stdout = open(os.devnull, 'w')
import pygame
# 重定向回原本的管道
sys.stdout = sys.__stdout__




import win32api 
import win32con
# 自动开启大写，从而避免中文输入法导致卡顿
is_capslock_pressed = win32api.GetKeyState(win32con.VK_CAPITAL)
if(not is_capslock_pressed):
    win32api.keybd_event(20,0,0,0)


# ==========参数加载模块==========

def get_config():
    config = dict()
    for i in range(1,len(sys.argv)):
        arg = sys.argv[i]
        splite = arg.partition("=")
        config[splite[0]] = splite[2]
    return config

CONFIG = get_config()

# ==========数据记录模块==========
import json

def record(block_id,trial_id,name,value):
    data_type = type(value).__name__


    if(data_type=='tuple'):
        data_type = 'list'
        value = list(value)

    value = '"'+str(value)+'"'

    # 通过管道与Electron沟通
    sys.stdout.write('{'+'"experimentId":{0},"blockId":{1},"trialId":{2},"dataName":"{3}","dataType":"{4}","dataValue":{5}'.format(
            CONFIG["experimentId"],
            block_id,
            trial_id,
            name,
            data_type,
            value
        )+'}\n'#追加一个换行符，防止多条信息堆积在管道里导致无法解析为json
    )
