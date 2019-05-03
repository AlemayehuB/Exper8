import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Read in the data from file
ch, counts= loadtxt('/home/alemsolobog/Exper8/baf/co-60.tsv', unpack=True, skiprows=22)
A = 2.7388111285378938
dA = 0.010215429073924514
B = -0.15149686213879948
dB = 0.026780799475270723
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Co-60 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')

# textstr1 = "Element: Bi-207 \n Peak: 75.0 keV"
# textstr2 = "Element: Bi-207 \n Peak: 1769.7 keV"
# textstr3 = "Element: Ba-133 \n Peak: 302 keV"
textstr4 = "Compton Edge \n Peak: 1173.2 keV"
textstr5 = "Peak: 1173.2 keV"
textstr6 = "Compton Edge \n Peak: 1332.5 keV"
textstr7 = "Peak: 1332.5 keV\n"
# file1 = open("co.txt","a")
# for i in range(len(ch)):
#     x = str(ch[i]) +  " " + str(energy[i]) + " " + str(counts[i]) + "\n"
#     file1.write(x)
# ax1.annotate(textstr1, xy=(75, 27), xytext=(75, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr3, xy=(302, 103), xytext=(302, 25),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr4, xy=(356, 123), xytext=(500, 100),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr5, xy=(382, 133), xytext=(800, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr2, xy=(1769.7, 639), xytext=(1200, 639),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr5, xy=(1160, 740), xytext=(650, 650),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr4, xy=(930, 191), xytext=(500, 300),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr7, xy=(1316, 797), xytext=(1800, 600),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr6, xy=(1097, 116), xytext=(1497, 200),arrowprops=dict(arrowstyle="->"))
ax1.legend(loc='upper right')


ax1.set_xlim(energy.min()-25,energy.max()+25)

plt.savefig('co60.png')
# plt.show()
