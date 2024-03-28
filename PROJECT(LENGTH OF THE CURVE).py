

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
x_pts = [-4.0, -2.5, -1.5, 0, 1.25, 1.75, 2.25, 3.5]
y_pts = [0, 0.75, 2.75, 4, 3.5, 2.25, 1.00, 0]
print("Please enter original length of the wire:")
lent = float(input())
x_vals = np.linspace(-4, 2 * np.pi, 50)
y_vals = np.interp(x_vals, x_pts, y_pts)
plt.plot(x_pts, y_pts, 'o')
plt.plot(x_vals, y_vals, '-x')
plt.show()




splines = interpolate.splrep(x_pts, y_pts)
x_vals1 = np.linspace(-4, 2 * np.pi, 50)
y_vals1 = interpolate.splev(x_vals, splines)
#--------------------------------------------------------
def length(x, y, x1, l):
    a = []
    for i in range(49):
        if (x[i] >= x1[7]):
            break
        else:
            t = (x[i + 1] - x[i]) * (x[i + 1] - x[i])
            g = (y[i + 1] - y[i]) * (y[i + 1] - y[i])
            a.append(np.sqrt(t + g))

    result = 0
    for i in range(len(a)):
        result = result + a[i]
    print(result)
    print("Difference")
    print(l - result)
#-----------------------------------------------------------

plt.plot(x_pts, y_pts, 'o', x_vals, y_vals, '-x', x_vals1, y_vals1, '-x')
plt.show()
print("Length of Polynomial Interpolation")
length(x_vals, y_vals, x_pts, lent)
print("Length of Spline Interpolation")
length(x_vals1, y_vals1, x_pts, lent)
print()
