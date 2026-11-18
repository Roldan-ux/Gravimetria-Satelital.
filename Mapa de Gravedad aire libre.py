import matplotlib.pyplot as plt
from data import generateData
import numpy as np
import csv
import os

path_basis = os.getcwd()
print(path_basis)

# target area
minlon1 =  -86.95;
maxlon1 =  -86.71;
minlat1 =  12.52;
maxlat1 =  12.70;

facX = 1.0;
facY = 1.0;
method = 'cubic'

# ya con X, Y, Z puede guardarlos o trabajarlos aca
X, Y, Z = generateData("gravity", minlon1, maxlon1, minlat1, maxlat1, facX, facY, method, path_basis)

fig, ax = plt.subplots()
im = ax.imshow(np.rot90(Z.T), extent=[X[0,0], X[0,-1], Y[-1,0], Y[0,0]], origin='lower', aspect='equal', vmin=np.nanmin(Z), vmax=np.nanmax(Z))
im.set_cmap('jet')
ax.set(xlim=[minlon1, maxlon1], ylim=[minlat1, maxlat1], xlabel='Longitude [deg]', ylabel='Latitude [deg]', title='GGMplus Gravity disturbances (mGal)')
fig.colorbar(im)
ax.grid(True)

plt.show()

f = open('telica(prueba1).txt','w')
writer = csv.writer(f,delimiter=' ')
writer.writerow(['X','Y','Z'])

m, n = X.shape

for i in range(m):
    for j in range(n):
        writer.writerow([X[i,j],Y[i,j],Z[i,j]])

f.close()