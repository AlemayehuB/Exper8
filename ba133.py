import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
ch, E, counts= loadtxt('/home/alemsolobog/Exper8/baf/ba-133.tsv', unpack=True, skiprows=25)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Ba-133 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')

textstr3 = "Peak: 382 keV\n"
textstr2 = "Peak: 356 keV\n"
textstr1 = "Peak: 302 keV\n"
textstr4 = "Peak: 81 keV\n"
# file1 = open("ba.txt","a")
# for i in range(len(ch)):
#     x = str(ch[i]) +  " " + str(energy[i]) + " " + str(counts[i]) + "\n"
#     file1.write(x)

ax1.annotate(textstr1, xy=(281, 12372.0), xytext=(100, 15000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr2, xy=(336, 23312.0), xytext=(200, 20000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr4, xy=(62,111950.0), xytext=(62, 60000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr3, xy=(364,4028), xytext=(320, 25000),arrowprops=dict(arrowstyle="->"))


ax1.legend(loc='upper center')
#

ax1.set_xlim(0,400)

plt.savefig('ba133.png')
# plt.show()
