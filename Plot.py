#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:17:35 2025

@author: Mathew
"""

from os.path import dirname, join as pjoin
import numpy as np
from skimage.io import imread
from skimage import measure
from skimage.filters import threshold_local
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# This is the csv file to load

path_to_load=r"/Users/Mathew/Documents/Edinburgh Code/PSD_2D_Intensity_FRET_Plot/CA1sr_PSD93KO.csv"



# Load the file:
    
df = pd.read_csv(path_to_load)

# Extract the columns
x = df['Acceptor_mean_intensity']
y = df['FRET_efficiency']

x_bins = np.linspace(0,2000,100)
y_bins = np.linspace(0,1,100)
plt.hist2d(y, x, bins=[y_bins,x_bins],cmap='jet')
 # plt.colors.LogNorm()
plt.colorbar()
plt.xlabel('FRET Efficiency')
plt.ylabel('Acceptor Mean Intensity')


# Extract the coordinates and FRET efficiency
x_coords = df['centroid-X']
y_coords = df['centroid-Y']
fret_efficiency = df['FRET_efficiency']

# Create a scatter plot
plt.figure(figsize=(8, 6))
scatter = plt.scatter(x_coords, y_coords, c=fret_efficiency, cmap='viridis', vmin=0, vmax=1)
plt.colorbar(scatter, label='FRET Efficiency')

# Add labels and title
plt.xlabel('Centroid X')
plt.ylabel('Centroid Y')
plt.title('Scatter Plot with FRET Efficiency as Color')

plt.show()