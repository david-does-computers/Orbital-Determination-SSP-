import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import odlib
import csv
from astropy.io import fits

plt.rcParams.update({
    "font.family": "Serif",
})

sns.set_theme(rc={'figure.figsize':(11.7,9), 'font.size': 50})

# filenames = ['astrometry/corr_Img1.fits', 'astrometry/corr_Img2.fits', 'astrometry/corr_Img3.fits']
# RMSRas = []
# RMSDecs = []
# for file in range(len(filenames)):
#     table = fits.open(filenames[file])[1].data

#     N = int(table.shape[0])
#     differenceSumRA = 0
#     differenceSumDec = 0
#     for i in range(N):
#         differenceSumRA += (table.field_ra[i] - table.index_ra[i])**2
#         differenceSumDec += (table.field_dec[i] - table.index_dec[i])**2

#     RMSRa = np.sqrt(differenceSumRA / N)
#     RMSDec = np.sqrt(differenceSumDec / N)

#     RMSRas.append(RMSRa)
#     RMSDecs.append(RMSDec)


# monte_carlo_699 = MonteCarlo(
#     np.array([np.radians(odlib.HMS2deg(14, 57, 18.79,)), np.radians(odlib.HMS2deg(14, 56, 43.69)), np.radians(odlib.HMS2deg(14, 56, 31.75))]),
#     np.array([np.radians(odlib.DMS2deg(-15, 8, 54.3)), np.radians(odlib.DMS2deg(-14, 50, 31.6)), np.radians(odlib.DMS2deg(-12, 58, 50.0))]),
#     np.array([odlib.date2JD('2024-06-23 4:45:22.282'), odlib.date2JD("-06-25 4:23:15.057"), odlib.date2JD("2024-07-10 4:29:37.678")]),
#     np.array([np.radians(value) for value in RMSRas]),
#     np.array([np.radians(value) for value in RMSDecs])
#     )

# elements = monte_carlo_699.iterative_error_calculation(100000)
# RMSRas.insert(2, 0.00010800512293802188)
# RMSDecs.insert(2, 8.503448641361101e-05)

# RAs = np.array([(odlib.HMS2deg(14, 57, 18.79,)), (odlib.HMS2deg(14, 56, 43.69)), odlib.HMS2deg(14, 55, 45.66), (odlib.HMS2deg(14, 56, 31.75))])
# DECs = np.array([(odlib.DMS2deg(-15, 8, 54.3)), (odlib.DMS2deg(-14, 50, 31.6)), odlib.DMS2deg(-13, 47, 26.5), (odlib.DMS2deg(-12, 58, 50.0))])
# RA_sigmas = np.array(RMSRas)
# DEC_sigmas = np.array(RMSDecs)

# print(RAs, DECs, RA_sigmas, DEC_sigmas)

# plt.errorbar(RAs, DECs, RA_sigmas,DEC_sigmas)
# plt.show()


# fields = ["a", "e", "i", "Om", "w", "T"]

# filename = "monte_carlo_data.csv"

# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)

#     csvwriter.writerows(elements)






elements = []

with open("monte_carlo_data.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        elements.append(row)


fields = ["Semi-Major Axis", "Eccentricity", "Inclination", "Long. Asc. Node", "Argument of Perihelion", "Time of Perihelion Passage"]
units = [" [AU]", "", " [deg]", " [deg]", " [deg]", " [JD-2450000]"]
jpl_elements = (2.612269855121786, .4099557226790182, 15.2974166959058, 242.5464403202016, 91.4775218652596)
calculated_elements = (2.6090275933683564, 0.38967323455652847, 16.537323323461283, 242.04582558916627, 93.41637556787789, 2459143.690855466-2450000)

elements = np.array(elements[1:], dtype=np.float64)
elements[:, 2:-1] *= 180 / np.pi
elements[:, -1] -= 2450000
means = np.array([np.mean(elements[:, i]) for i in range(6)])
sigmas = np.array([np.std(elements[:, i]) for i in range(6)])
print(sigmas)

for i in range(6):
    ax = sns.histplot(elements[:, i], bins=100, kde="True", stat="probability")
    kde = ax.get_lines()[-1]
    x, y = kde.get_data()
    mask1 = (means[i] - sigmas[i]) < x
    x, y = x[mask1], y[mask1]
    mask2 = x < (means[i] + sigmas[i])
    x, y = x[mask2], y[mask2]
    ax.fill_between(x, y1=y, alpha=0.3, facecolor='#663399')
    plt.axvline(calculated_elements[i], linewidth=4, color="#385287")
    if i < len(jpl_elements):
        plt.axvline(jpl_elements[i], linewidth=4, color="#dc4a42")
        plt.legend(["_", "_", "Calculated Value", "JPL Value"], loc="upper right", fontsize=17)
    else:
        plt.legend(["_", "_", "Calculated Value"], loc="upper right",fontsize=17)
    
    print(means[i] - sigmas[i], means[i] + sigmas[i])
    plt.xlabel(fields[i] + units[i], fontdict={"size": 20})
    plt.ylabel("Probability", fontdict={"size": 20})
    plt.xticks(fontsize=17)
    plt.yticks(fontsize=17)
    plt.title(f"Monte Carlo {fields[i]} Distribution", fontdict={"size": 25})
    print(f"Std Dev in {fields[i]}: {sigmas[i]}")
    plt.show()
