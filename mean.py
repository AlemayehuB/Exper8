import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
E, T, dE, dT= loadtxt('/home/alemsolobog/Exper8/disper.txt', unpack=True, skiprows=1)
E = np.sort(E)
T = np.sort(T)
dE = np.sort(dE)
dT = np.sort(dT)
mc = ((2*E) * (E -T))/T  #keV/c^2
dmc = mc * np.sqrt(np.sqrt(np.power((2*dE)/(2*E),2) + np.power(np.sqrt(np.power(dE, 2) + np.power(dT,2))/(E -T),2)) + np.power(dT/T,2))
print(m)


##############################################################################
# Fit
##############################################################################
p01 = [10,6]
pf1, cov1, info1, mesg1, success1 = optimize.leastsq(residual, p01,
                                     args = (E, mc, dmc), full_output=1)

if cov1 is None:
    print('Fit did not converge')
    print('Success code:', success1)
    print(mesg1)
else:
    print('Fit Converged')
    chisq1 = sum(info1['fvec']*info1['fvec'])
    dof1 = len(E)-len(pf1)
    pferr1 = [np.sqrt(cov1[i,i]) for i in range(len(pf1))]
    print('Converged with chi-squared', chisq1)
    print('Number of degrees of freedom, dof =',dof1)
    print('Reduced chi-squared:', chisq1/dof1)
    print('Inital guess values:')
    print('  p0 =', p01)
    print('Best fit values:')
    print('  pf =', pf1)
    print('Uncertainties in the best fit values:')
    print('  pferr =', pferr1)
    print()

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.errorbar(E, mc, yerr = dmc, xerr = dE, fmt='k.', label = 'Data')
    T = np.linspace(E.min(), E.max(), 500)
    ax1.plot(T, fitfunc(pf1, T), 'r-', label = 'Fit')

    ax1.set_title('Mass of the Electron from Non-Relativistic Dispersion Relation')
    ax1.set_xlabel('Energy, $keV$')
    ax1.set_ylabel('$m_{nr} = p^{2}/2T, keV/c^{2}$')
    ax1.legend()

    textfit = '$g(T) =  A* T + B $ \n' \
              '$A = %.3f \pm %.3f$ ch/E \n' \
              '$B = %.1f \pm %.1f$ ch \n' \
              '$\chi^2= %.2f$ \n' \
              '$N = %i$ (dof) \n' \
              '$\chi^2/N = % .2f$ \n' \
               % (pf1[0], pferr1[0],pf1[1],pferr1[1], chisq1, dof1,
                  chisq1/dof1)



    ax1.legend(loc='lower right')
    ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
            verticalalignment='top')
    ax1.set_xlim(E.min()-25,E.max()+25)

    plt.savefig('disper.png')
    plt.show()
