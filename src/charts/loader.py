import matplotlib.pyplot as plt
from io import BytesIO
import base64
import sys
import json

# ==========参数加载模块==========

def get_config():
    config = dict()
    for i in range(1,len(sys.argv)):
        arg = sys.argv[i]
        split = arg.partition("=")
        try:#如果是数组或json对象就自动加载
            config[split[0]] = json.loads(split[2])
        except:#如果加载失败就变成字符串
            config[split[0]] = split[2]
    return config

CONFIG = get_config()

# ==========数据记录模块==========

def output(plt):
    buffer = BytesIO()
    plt.savefig(buffer,format="png")
    data_url = base64.b64encode(buffer.getvalue()).decode('utf8')#从Bytes转化成string
    print(data_url)