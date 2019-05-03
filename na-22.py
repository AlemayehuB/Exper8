import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
ch, E, counts= loadtxt('/home/alemsolobog/Exper8/baf/2nd_na-22.tsv', unpack=True, skiprows=25)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Na-22 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')

# textstr2 = "Element: Bi-207 \n Peak: 1769.7 keV"
# textstr3 = "Element: Ba-133 \n Peak: 302 keV"
textstr4 = "Compton Edge \n Peak: 1274.6 keV"
textstr5 = "Peak: 1274.6 keV"
textstr6 = "Compton Edge \n Peak: 511 keV"
textstr7 = "Peak: 511 keV\n"
file1 = open("na.txt","a")
for i in range(len(ch)):
    x = str(ch[i]) +  " " + str(energy[i]) + " " + str(denergy[i])+ " " + str(counts[i]) + "\n"
    file1.write(x)

# ax1.annotate(textstr1, xy=(75, 27), xytext=(75, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr3, xy=(302, 103), xytext=(302, 25),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr4, xy=(356, 123), xytext=(500, 100),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr5, xy=(382, 133), xytext=(800, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr2, xy=(1769.7, 639), xytext=(1200, 639),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr6, xy=(300, 760), xytext=(100, 1300),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr7, xy=(511, 6802), xytext=(600, 6000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr5, xy=(1275, 1119), xytext=(1575, 1119),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr4, xy=(1020, 155), xytext=(800, 1500),arrowprops=dict(arrowstyle="->"))
ax1.legend(loc='upper right')


ax1.set_xlim(energy.min()-25,energy.max()+25)

plt.savefig('na22.png')
# plt.show()
