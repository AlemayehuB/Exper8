import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
ch, E, counts= loadtxt('/home/alemsolobog/Exper8/baf/2nd_na-22.tsv', unpack=True, skiprows=25)
A = 2.7367304419009835
dA = 0.01020778294056433
B = -0.15117286764211035
dB = 0.026667468601821422
energy = ch * A + B
denergy = ch * dA + dB
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(energy, counts,denergy,fmt="r.", label = "Data")

ax1.set_title('Na-22 Decay Spectrum')
ax1.set_xlabel('Energy, $keV$')
ax1.set_ylabel('Counts')

# textstr1 = "Element: Bi-207 \n Peak: 75.0 keV"
# textstr2 = "Element: Bi-207 \n Peak: 1769.7 keV"
# textstr3 = "Element: Ba-133 \n Peak: 302 keV"
# textstr4 = "Element: Ba-133 \n Peak: 356 keV"
# textstr5 = "Element: Ba-133 \n Peak: 382 keV"
textstr6 = "Compton Edge: Peak: 511 keV "
textstr7 = "Peak: 511 keV"
#
# ax1.annotate(textstr1, xy=(75, 27), xytext=(75, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr3, xy=(302, 103), xytext=(302, 25),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr4, xy=(356, 123), xytext=(500, 100),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr5, xy=(382, 133), xytext=(800, 200),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr2, xy=(1769.7, 639), xytext=(1200, 639),arrowprops=dict(arrowstyle="->"))
# ax1.annotate(textstr6, xy=(1170, 424), xytext=(1400, 339),arrowprops=dict(arrowstyle="->"))
ax1.annotate(textstr7, xy=(511, 6802), xytext=(600, 6000),arrowprops=dict(arrowstyle="->"))
ax1.legend(loc='upper right')


ax1.set_xlim(energy.min()-25,energy.max()+25)

plt.savefig('na22.png')
plt.show()
