import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from matplotlib.widgets import Cursor

m=(0,0.0025,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.07,0.085,0.1,0.104)
n = (25,444,484,540,567,590,610,622,636,644,652,660,666,689,706,720,727)

a=np.linspace(0,0.15,100000)
def func(x):
    return 69.39 * np.log(5674.02*x**2+ 1300.33 * x +0.01) +358.05

y= [func(x) for x in a]

fig, ax = plt.subplots()
ax.plot(m, n, 'k.')
ax.plot(a, y, 'g')
cursor = Cursor(ax, useblit=True, color='red', linewidth=0.5)
plt.show()
