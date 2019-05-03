import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
ch, E, counts= loadtxt('/home/alemsolobog/Exper8/baf/In-116.tsv', unpack=True, skiprows=25)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('In-116 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')


textstr2 = "Compton Edge \n Peak: 1097.2 keV"
textstr1 = "Peak: 1097.2 keV\n"
textstr3 = "Compton Edge \n Peak: 1293.3 keV"
textstr4 = "Peak: 1293.3 keV\n"

file1 = open("in.txt","a")
for i in range(len(ch)):
    x = str(ch[i]) +  " " + str(energy[i]) + " " + str(denergy[i])+ " " + str(counts[i]) + "\n"
    file1.write(x)

ax1.annotate(textstr1, xy=(1084, 1466), xytext=(900, 1000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr2, xy=(846, 336), xytext=(92, 1000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr3, xy=(1059,257), xytext=(2000, 400),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr4, xy=(1293.3, 1790), xytext=(1500, 1500),arrowprops=dict(arrowstyle="->"))

ax1.legend(loc='upper right')
#
ax1.set_xlim(energy.min(),energy.max())
ax1.set_ylim(0,counts.max())
plt.savefig('in116.png')
# plt.show()
