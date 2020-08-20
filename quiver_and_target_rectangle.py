import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

import pandas as pd

import rectangle

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(rectangle.verts, codes)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_title('BFP/kg')
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)

fit = pd.read_csv("fit.csv", float_precision='high')

fit['weight'] = (fit['weight'].str.split()).apply(
    lambda x: float(x[0].replace(',', '.')))
fit['weight'] = fit['weight'].astype(float)

fit['bfp'] = (fit['bfp'].str.split()).apply(
    lambda x: float(x[0].replace(',', '.')))
fit['bfp'] = fit['bfp'].astype(float)

# plt.scatter(fit['weight'][0], fit['bfp'][0], color='orange', marker='*')

for i in range(len(fit.index) - 1):
    ax.quiver(fit['weight'][i], fit['bfp'][i], fit['weight'][i + 1] - fit['weight'][i], fit['bfp']
              [i + 1] - fit['bfp'][i], color='red', scale_units='xy', angles='xy', scale=1, width=0.001)

ax.quiver(fit['weight'][0], fit['bfp'][0], fit['weight'][len(fit.index) - 1] - fit['weight'][0], fit['bfp']
          [len(fit.index) - 1] - fit['bfp'][0], color='blue', scale_units='xy', angles='xy', scale=1, width=0.005)

plt.xlim(61, 73)
plt.ylim(9, 19)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
