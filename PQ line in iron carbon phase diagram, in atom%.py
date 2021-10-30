import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from matplotlib.widgets import Cursor


x=(0,0.0025,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.07,0.085,0.1,0.104)
y = (25,444,484,540,567,590,610,622,636,644,652,660,666,689,706,720,727)

fig, ax = plt.subplots()
ax.plot(x, y, 'k.')

def target_func(x,a0, b2, a1, a2, a3):
    return a0 * np.log(b2*x**2+a1 * x +a2) + a3
def line(x, k, b0):
    return k * x + b0

#a0 = max(y) - min(y)
#a1 = x[round(len(x) / 2)]
#a2 = x[round(len(x) / 2)]
#a3 = min(y)
#ar = [a0, a1, a2, a3]

k=(max(y)-min(y))/(max(x)-min(x))
b0= min(y)
p_line=[k, b0]

para, cov = optimize.curve_fit(target_func, x, y,maxfev=100000000)
para_1, cov_1 = optimize.curve_fit(line, x, y, p0=p_line)

print(para)
print(para_1)

y_fit = [target_func(a, *para) for a in x]
y_fit_1 = [line(c, *para_1) for c in x]
print(y_fit)
print(y_fit_1)

ax.plot(x, y_fit)
ax.plot(x, y_fit_1, 'g')
cursor = Cursor(ax, useblit=True, color='red', linewidth=0.5)

plt.show()
