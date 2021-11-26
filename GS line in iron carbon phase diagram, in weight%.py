import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from matplotlib.widgets import Cursor

pi = np.pi
# 模拟生成一组实验数据
x = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.77)
y = (912, 877, 840, 800, 780, 760, 740, 727)
fig, ax = plt.subplots()
ax.plot(x, y, 'b.')


# 拟合指数曲线
def target_func(x, a0, a1, a2, a3):
    return a0 * np.exp(-a1 * x**2 - a2 * x) + a3


a0 = max(y) - min(y)
a1 = x[round(len(x) / 2)]
a2 = x[round(len(x) / 2)]
a3 = min(y)
ar = [a0, a1, a2, a3]
para, cov = optimize.curve_fit(target_func, x, y, p0=ar)
y_fit = [target_func(a, *para) for a in x]
corr_corf = np.corrcoef(y, y_fit)
print(cov)
print(para)
print(y_fit)
print(corr_corf)
ax.plot(x, y_fit)
r2 = 'R^2=' + str(corr_corf[0, 1])
equation = 'y=' + str(para[0]) + '\nexp[-' + str(para[1]) + 'x^2\n-' + str(
    para[2]) + 'x]\n+' + str(para[3])
plt.title("GS line in iron-carbon phase diagram, in wt.%", fontsize=18)
plt.text(0.01, 730, r2, fontsize=16)
plt.text(0.25,
         850,
         equation + '\n\n \'x\' in this equation represents wt.%',
         fontsize=16)
cursor = Cursor(ax, useblit=True, color='red', linewidth=0.5)
plt.show()
