# -*- coding: utf-8 -*-
"""
Created on Thu May 11 17:21:11 2023

@author: gcorn
"""

import csv
import io
import pandas as pd
from pathlib import Path


HERE = Path(__file__).parent
TO_DATASETS = HERE / 'datasets'


# Opens the earthquake data file.
filename = TO_DATASETS / 'earthquakes_data.csv'

lats, lons = [], []


    
df = pd.read_csv(filename)
column_data = df['latitude']

print('lats', column_data)

# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.fillcontinents(color = 'gray')
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
x,y = eq_map(lons, lats)
eq_map.plot(x, y, 'ro', markersize=6)
 
plt.show()