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

para, cov = optimize.curve_fit(target_func, x, y,maxfev=900000000)

print(para)
print(cov)

y_fit = [target_func(a, *para) for a in x]

corr_corf=np.corrcoef(y,y_fit)
print(y_fit)
print(corr_corf)

r2='R^2='+str(corr_corf[0,1])
equation='y='+str(para[0])+'*\nln[-'+str(para[1])+'x^2\n+'+str(para[2])+'x+'+str(para[3])+']+'+str(para[4])
plt.text(0.03,505,r2,fontsize=16)
plt.text(0,400,equation,fontsize=16)
ax.plot(x, y_fit)
cursor = Cursor(ax, useblit=True, color='red', linewidth=0.5)

plt.show()
