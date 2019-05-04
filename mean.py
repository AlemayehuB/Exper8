import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt


# Read in the data from file
E, T, dE, dT= loadtxt('/home/alemsolobog/Exper8/disper.txt', unpack=True, skiprows=1)
# E = np.sort(E)
# T = np.sort(T)
# dE = np.sort(dE)
# dT = np.sort(dT)
mc = ((2*E) * (E -T))/T  #keV/c^2
dmc = mc * np.sqrt(np.power((2*dE)/(2*E),2) + np.power(np.sqrt(np.power(dE, 2) + np.power(dT,2))/(E -T),2) + np.power(dT/T,2))


w = 1/(np.power(dmc,2))
x = np.sum(w*mc)/np.sum(w)
sig =  np.sqrt(1/np.sum(w))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
ax1.errorbar(E, mc, yerr = dmc, xerr = dE, fmt='k.', label = 'Data')
T = np.linspace(E.min(), E.max(), 500)
ax1.plot(T, [x] * len(T), 'r-', label = 'Weighted Mean = %.5f' %(x))


ax1.set_title('Rest Energy of Electron')
ax1.set_xlabel('T, $keV$')
ax1.set_ylabel('$m_{0}c^{2}$')
ax1.legend()


ax1.legend(loc='lower right')
textfit = '$Standard Deviation in Mean of $m_{0}c^{2} = %.5f$' %(sig)
ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
        verticalalignment='top')
ax1.set_xlim(E.min()-25,E.max()+25)

plt.savefig('mean.png')
plt.show()
