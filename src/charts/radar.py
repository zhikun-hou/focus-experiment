from loader import *

# 导入第三方模块
import numpy as np
import matplotlib.pyplot as plt

# 中文和负号的正常显示
plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'
plt.rcParams['axes.unicode_minus'] = False

# 使用ggplot的绘图风格
plt.style.use('ggplot')

# 构造数据
values = CONFIG["values"]
feature = ['个人能力','QC知识','解决问题能力','服务质量意识','团队精神']

N = len(values)
# 设置雷达图的角度，用于平分切开一个圆面
angles=np.linspace(0, 2*np.pi, N, endpoint=False)
# 为了使雷达图一圈封闭起来，需要下面的步骤
values=np.concatenate((values,[values[0]]))
angles=np.concatenate((angles,[angles[0]]))
feature=np.concatenate((feature,[feature[0]]))

# 绘图
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=2, label = '活动前')
# 填充颜色
ax.fill(angles, values, alpha=CONFIG["alpha"])

# 添加每个特征的标签
ax.set_thetagrids(angles * 180/np.pi, feature)
# 设置雷达图的范围
ax.set_ylim(0,5)
# 添加标题
plt.title(CONFIG["title"])

# 添加网格线
ax.grid(True)
# 设置图例
plt.legend(loc = 'best')
# 显示图形

output(plt)