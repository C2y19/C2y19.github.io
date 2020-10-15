import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0,10,0.1)
e= math.e
y = e**-x**0.6
plt.title("指数函数")
plt.plot(x, y)
plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.show()
