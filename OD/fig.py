import numpy as np
import odlib
from astropy.io import fits
import matplotlib.pyplot as plt


filenames = ['astrometry/corr_Img1.fits', 'astrometry/corr_Img2.fits', 'astrometry/corr_Img3.fits']
RMSRas = []
RMSDecs = []
for file in range(len(filenames)):
    table = fits.open(filenames[file])[1].data

    N = int(table.shape[0])
    differenceSumRA = 0
    differenceSumDec = 0
    for i in range(N):
        differenceSumRA += (table.field_ra[i] - table.index_ra[i])**2
        differenceSumDec += (table.field_dec[i] - table.index_dec[i])**2

    RMSRa = np.sqrt(differenceSumRA / N)
    RMSDec = np.sqrt(differenceSumDec / N)

    RMSRas.append(RMSRa)
    RMSDecs.append(RMSDec)

RMSRas.insert(2, 0.00010800512293802188)
RMSDecs.insert(2, 8.503448641361101e-05)

RAs = np.array([(odlib.HMS2deg(14, 57, 18.79,)), (odlib.HMS2deg(14, 56, 43.69)), odlib.HMS2deg(14, 55, 45.66), (odlib.HMS2deg(14, 56, 31.75))])
DECs = np.array([(odlib.DMS2deg(-15, 8, 54.3)), (odlib.DMS2deg(-14, 50, 31.6)), odlib.DMS2deg(-13, 47, 26.5), (odlib.DMS2deg(-12, 58, 50.0))])
RA_sigmas = np.array(RMSRas)
DEC_sigmas = np.array(RMSDecs)

print(RAs, DECs, RA_sigmas, DEC_sigmas)

plt.errorbar(RAs, DECs, xerr=100*RA_sigmas, yerr=1000*DEC_sigmas,  capsize=3, fmt="r--o", ecolor = "black")
plt.show()