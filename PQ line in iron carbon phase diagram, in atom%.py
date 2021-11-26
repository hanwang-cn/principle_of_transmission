import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from matplotlib.widgets import Cursor

a=(0,0.0025,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.07,0.085,0.1,0.104)
y = (25,444,484,540,567,590,610,622,636,644,652,660,666,689,706,720,727)

fig, ax = plt.subplots()
ax.plot(a, y, 'k.')

def target_func(x,a0, b2, a1, a2, a3):
    return a0 * np.log(b2*x**2+a1 * x +a2) + a3

para, cov = optimize.curve_fit(target_func, a, y,maxfev=900000000)

print(para)
print(cov)

y_fit = [target_func(data, *para) for data in a]

corr_corf=np.corrcoef(y,y_fit)
print(y_fit)
print(corr_corf)

r2='R^2='+str(corr_corf[0,1])
equation='y='+str(para[0])+'*\nln[-'+str(para[1])+'a^2\n+'+str(para[2])+'a\n+'+str(para[3])+']\n+'+str(para[4])
plt.text(0.03,105,r2,fontsize=16)
plt.text(0.015,230,equation+'\n\nwhile a is at.%, not the wt.%',fontsize=16)
ax.plot(a, y_fit)
cursor = Cursor(ax, useblit=True, color='red', linewidth=0.5)

plt.show()
