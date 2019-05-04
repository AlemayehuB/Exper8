import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
E, T, dE, dT= loadtxt('/home/alemsolobog/Exper8/disper.txt', unpack=True, skiprows=1)

p = 2 *E - T
dp = np.sqrt(np.power(dE*2,2) + np.power(dT,2))
def non_rel(b):
    return np.power(b,2)/(2*511)
def rel(b):
    return (np.sqrt(np.power(511,2) + np.power(b,2)) - 511 )

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(p, T, yerr = dT, xerr = dp, fmt='k.', label = 'Data')
T = np.linspace(p.min(), p.max(), 500)

ax1.plot(T,rel(T) , 'r--', label = 'Relativistic Form')
ax1.plot(T,non_rel(T) , 'b--', label = 'Relativistic Form')

ax1.set_title(' Experimentally Determinded Dispersion Relation \n Overlaid with Relativistic and Non-Relativistic Dispersion Relation')
ax1.set_xlabel('p, $keV/c$')
ax1.set_ylabel('T, $keV$')
ax1.legend()


ax1.legend(loc='lower right')
# textfit = '$Standard Deviation in Mean of $m_{0}c^{2} = %.5f$' %(sig)
# ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
#         verticalalignment='top')
ax1.set_xlim(p.min(),p.max())

plt.savefig('tvp.png')
plt.show()
