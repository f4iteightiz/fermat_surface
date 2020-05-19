# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 14:53:19 2019
draw of a Fermat cubic surface with matplotlib
https://en.wikipedia.org/wiki/Fermat_cubic
X^3 + Y^3 + Z^3 = 1
Pierre de Fermat, French, End 1607 - 12 January 1665
@author: pas
"""
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# formula used for the curve
# X^3 + Y^3 + Z^3 = N
# N = 1 is the basic fermat surface. Other Ns are variants
N = 10
# coordinate area for the 3D representation -Wide till +Wide in X and Y 
Wide = 8
#
# Make data.
X = np.arange(-Wide, Wide, 0.01)
Y = np.arange(-Wide, Wide, 0.01)
X, Y = np.meshgrid(X, Y)
#
#could be another surface
#R = np.sqrt(X**2 + Y**2)  
#Z = np.sin(R)             
#
Z = np.cbrt(N-X**3-Y**3)   # cubic root of Z dim of the Fermat cubic surface
#
# Plot the surface.
# colormaps examples https://matplotlib.org/tutorials/colors/colormaps.html
#surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                       linewidth=0, antialiased=False)
surf = ax.plot_surface(X, Y, Z, cmap=cm.winter,
                       linewidth=0, antialiased=False)
# showing the axis to be sure when it turns in 3D
ax.set_xlabel('X dim')
ax.set_ylabel('Y dim')
ax.set_zlabel('Z dim')
#
# Customize the z axis and its limits for the 3D representation
Windo= (N+Wide**3+Wide**3)**(1/3)
ax.set_zlim(-Windo, Windo)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
#
plt.show()