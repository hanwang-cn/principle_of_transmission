import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
pi = np.pi
# 模拟生成一组实验数据
x = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.77)
y = (912, 877, 840, 800, 780, 760, 740, 727)
fig, ax = plt.subplots()
ax.plot(x, y, 'b.')
# 拟合指数曲线
def target_func(x, a0, a1, a2, a3):
    return a0 * np.exp(- a1*x**2 - a2 * x ) + a3
a0 = max(y) - min(y)
a1 = x[round(len(x) / 2)]
a2 = x[round(len(x) / 2)]
a3 = min(y)
ar = [a0, a1, a2, a3]

para, cov = optimize.curve_fit(target_func, x, y, p0=ar)


y_fit = [target_func(a, *para) for a in x]
corr_corf=np.corrcoef(y,y_fit)


print(cov)
print(para)
#print(r_squared)

print(y_fit)
print(corr_corf)

ax.plot(x, y_fit)

plt.show()
