import sys
import os
import json
import mne
import sqlite3

# 必须在数据分析算法前面加from loader import *，然后使用CONFIG获取参数


# ==========参数加载模块==========

def get_config():
    config = dict()
    for i in range(1,len(sys.argv)):
        arg = sys.argv[i]
        splite = arg.partition("=")
        config[splite[0]] = splite[2]
    return config

CONFIG = get_config()

# ==========结果输出模块==========

def output(obj):
    print(
        json.dumps(obj)
    )

# ==========edf文件加载模块==========

def load_edf(path):
    mne.io.read_raw_edf(path,
        montage='deprecated', 
        eog=None,
        misc=None,
        stim_channel='auto',
        exclude=(), 
        preload=False, 
        verbose=None)


# ==========sqlite数据库加载模块==========

def load_data(db_path,statement):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    cursor.execute(statement)

    data = cursor.fetchall()

    cursor.close()
    con.close()

    return data
