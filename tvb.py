import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
E, T, dE, dT= loadtxt('/home/alemsolobog/Exper8/disper.txt', unpack=True, skiprows=1)

B = (T * (2 * E - T))/(np.power(T,2) - 2*E*T + 2*np.power(E,2))
dB = ((4 * E) *(E-T) * np.sqrt(np.power(E*dT,2) + np.power(T*dE,2)))/np.power((np.power(T,2) - (2*T*E) + 2*(np.power(E,2))),2)

def t_t(b):
    return 511 * ((1/np.sqrt(1-np.power(b,2)))-1)


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(B, T, yerr = dT, xerr = dB, fmt='k.', label = 'Data')
T = np.linspace(B.min(), 0.97, 500)
ax1.plot(T,t_t(T) , 'r--', label = 'Expected Form')


ax1.set_title(' Comparing Special Relativity Pred. & \n Experimental Data:T vs $\\beta $')
ax1.set_xlabel('$\\beta $')
ax1.set_ylabel('$p , keV$')
ax1.legend()


ax1.legend(loc='lower right')
# textfit = '$Standard Deviation in Mean of $m_{0}c^{2} = %.5f$' %(sig)
# ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
#         verticalalignment='top')
ax1.set_xlim(0.75,1)

plt.savefig('tvb.png')
plt.show()
