import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

from shapely.geometry import Polygon
from shapely.geometry import Point

import rectangle

poly = Polygon(rectangle.verts)

fit = pd.read_csv("fit.csv", float_precision='high')

fit['weight'] = (fit['weight'].str.split()).apply(
    lambda x: float(x[0].replace(',', '.')))
fit['weight'] = fit['weight'].astype(float)

fit['bfp'] = (fit['bfp'].str.split()).apply(
    lambda x: float(x[0].replace(',', '.')))
fit['bfp'] = fit['bfp'].astype(float)

fit['day'] = pd.to_datetime(fit['day'])

fit['distance'] = fit.apply(lambda x: 0.0, axis=1)
fit['n'] = fit.apply(lambda x: fit['day'][0], axis=1)

for i in range(len(fit.index)):
    point = Point(fit['weight'][i], fit['bfp'][i])
    fit.loc[i, 'distance'] = point.distance(poly)
    fit.loc[i, 'n'] = (fit.loc[i, 'day'] - fit.loc[i, 'n']).days

fit.plot(x='n', y='distance', kind='line')

plt.grid(True)
plt.show()
