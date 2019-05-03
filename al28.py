import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
ch, enerr, counts= loadtxt('/home/alemsolobog/Exper8/baf/al-28.tsv', unpack=True, skiprows=25)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Al-28 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')


textstr2 = "Compton Edge \n Peak: 661.6 keV"
textstr1 = "Peak: 178 keV\n"

file1 = open("al.txt","a")
for i in range(len(ch)):
    x = str(ch[i]) +  " " + str(energy[i]) + " " + str(counts[i]) + "\n"
    file1.write(x)

ax1.annotate(textstr1, xy=(640, 8500), xytext=(400, 7000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr2, xy=(443, 815), xytext=(300, 1500),arrowprops=dict(arrowstyle="->"))
ax1.legend(loc='upper right')
#
# ax1.set_ylim(0,1000)
ax1.set_xlim(energy.min(),energy.max())

plt.savefig('al28.png')
# plt.show()
