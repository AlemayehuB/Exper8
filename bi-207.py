import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
ch,E, counts= loadtxt('/home/alemsolobog/Exper8/baf/2nd_bi-207.tsv', unpack=True, skiprows=25)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Bi-207 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')

textstr1 = "Peak: 75.0 keV"
textstr2 = "Peak: 569.6 keV"
textstr3 = "Peak: 1060 keV"
textstr4 = "Peak: 1769.7 keV"
textstr5 = "Compton Edge \n Peak: 569.6 keV"
textstr6 = "Compton Edge \n Peak: 1060 keV"

# file1 = open("bi.txt","a")
# for i in range(len(ch)):
#     x = str(ch[i]) +  " " + str(energy[i]) + " " + str(counts[i]) + "\n"
#     file1.write(x)

ax1.annotate(textstr1, xy=(66, 9366), xytext=(100, 8666),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr2, xy=(550, 3088), xytext=(302, 5000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr5, xy=(366, 290), xytext=(250, 1000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr3, xy=(1051, 668), xytext=(1000, 2000),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr6, xy=(821, 122), xytext=(1300, 639),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr4, xy=(1750, 39), xytext=(1750, 3000),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr7, xy=(511, 6802), xytext=(600, 6000),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr5, xy=(1275, 1119), xytext=(1575, 1119),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr4, xy=(1020, 155), xytext=(800, 1500),arrowprops=dict(arrowstyle="->"))
ax1.legend(loc='upper right')

ax1.set_xlim(energy.min(),energy.max())
ax1.set_ylim(0,10000)

plt.savefig('bi207.png')
# plt.show()
