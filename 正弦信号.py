import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x=np.arange(0,2*np.pi,0.01)
y=np.sin(x)
plt.title("正弦函数")
plt.plot(x,y)
plt.show()
