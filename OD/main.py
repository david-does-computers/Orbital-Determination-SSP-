import numpy as np
import odlib
from Observation import Observation
from OrbitDetermination import OrbitDetermination
from EphemerisGeneration import EphemerisGeneration
from GaussMethod import GaussMethod
from MonteCarlo import MonteCarlo
from astropy.io import fits
import csv

# K = 0.0172020989484

# myGauss = GaussMethod((
#     Observation(np.radians(odlib.HMS2deg(15, 48, 6.22)), np.radians(odlib.DMS2deg(-2, 46, 44.3)), 2460118.708333333),
#     Observation(np.radians(odlib.HMS2deg(15, 50, 18.27)), np.radians(odlib.DMS2deg(1, 12, 55.0 )), 2460125.708333333),
#     Observation(np.radians(odlib.HMS2deg(15, 57, 23.59)), np.radians(odlib.DMS2deg(6, 7, 24.6)), 2460132.708333333)
#     ))


# myGauss.iterative_honing(1e-10)
# print(myGauss.get_equatorial_vectors())
# myOD = OrbitDetermination(*myGauss.get_ecplitic_vectors(), 2460125.708333333)
# print(myOD.get_orbital_elements_dict())
# myEphem = EphemerisGeneration(*myOD.get_orbital_elements())
# print(np.degrees(myEphem.get_RA_DEC(2460511.75)[0]), np.degrees(myEphem.get_RA_DEC(2460511.75)[1]))

# testOD = OrbitDetermination(
#     np.array([0.39706319, -1.2250737, 0.47474252]),
#     np.array([0.01139883, 0.00267983, 0.00375085]) / 0.0172020989484,
#     2458313.5
# )
# print(testOD.get_orbital_elements_dict())

Gauss_699 = GaussMethod((
    Observation(np.radians(odlib.HMS2deg(14, 57, 18.79,)), np.radians(odlib.DMS2deg(-15, 8, 54.3)), odlib.date2JD('2024-06-23 4:45:22.282')),
    Observation(np.radians(odlib.HMS2deg(14, 56, 43.69)), np.radians(odlib.DMS2deg(-14, 50, 31.6)), odlib.date2JD("2024-06-25 4:23:15.057")),
    Observation(np.radians(odlib.HMS2deg(14, 56, 31.75)), np.radians(odlib.DMS2deg(-12, 58, 50.0)), odlib.date2JD("2024-07-10 4:29:37.678"))
))
Gauss_699.iterative_honing()
OD_699 = OrbitDetermination(*Gauss_699.get_ecplitic_vectors(), Gauss_699.corrected_times[1])
print(OD_699.get_orbital_elements())
Ephem_699 = EphemerisGeneration(*OD_699.get_orbital_elements())
RA, DEC = Ephem_699.get_RA_DEC(odlib.date2JD("2024-07-10 04:29:37.678"))
print(f"RA: {odlib.deg2HMS(np.degrees(RA))} -- DEC: {odlib.deg2DMS(np.degrees(DEC))}")


# EPOCH=  2457726.5 ! 2016-Dec-04.00 (TDB)         Residual RMS= .2481
#    EC= .4099557226790182   QR= 1.54135487883272    TP= 2457583.6199333891
#    OM= 242.5464403202016   W=  91.4775218652596    IN= 15.2974166959058
#    A= 2.612269855121786    MA= 33.35405646917018   ADIST= 3.683184831410852
#    PER= 4.22217            N= .233440936           ANGMOM= .025359197
#    DAN= 2.19646            DDN= 2.15051            L= 334.0782093
#    B= 15.2922062           MOID= .62554502         TP= 2016-Jul-14.1199333891



