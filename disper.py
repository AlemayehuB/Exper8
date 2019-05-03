import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
elm, E, T, dE, dT= loadtxt('/home/alemsolobog/Exper8/disper.txt', unpack=True, skiprows=1)


##############################################################################
# Fit
##############################################################################
p01 = [10,6]
pf1, cov1, info1, mesg1, success1 = optimize.leastsq(residual, p01,
                                     args = (E, ch, dch), full_output=1)

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
    ax1.errorbar(E, ch, dch, fmt='k.', label = 'Data')
    T = np.linspace(E.min(), E.max(), 500)
    ax1.plot(T, fitfunc(pf1, T), 'r-', label = 'Fit')

    ax1.set_title('Energy Calibration')
    ax1.set_xlabel('Energy, $keV$')
    ax1.set_ylabel('Channel')
    ax1.legend()

    textfit = '$ch(E) =  A\'*E + B\' $ \n' \
              '$A\' = %.3f \pm %.3f$ ch/E \n' \
              '$B\' = %.1f \pm %.1f$ ch \n' \
              '$\chi^2= %.2f$ \n' \
              '$N = %i$ (dof) \n' \
              '$\chi^2/N = % .2f$ \n' \
              '$A = %.2f \pm %.2f$ E/ch \n' \
              '$B = %.2f \pm %.2f$ E \n' \
               % (pf1[0], pferr1[0],pf1[1],pferr1[1], chisq1, dof1,
                  chisq1/dof1, 1/pf1[0], (pferr1[0]/pf1[0])*(1/pf1[0]),1/pf1[1], (pferr1[1]/pf1[1])*(1/pf1[1]))
    textstr1 = "Element: Bi-207 \n Peak: 75.0 keV"
    textstr2 = "Element: Bi-207 \n Peak: 1769.7 keV"
    textstr3 = "Element: Ba-133 \n Peak: 302 keV"
    textstr4 = "Element: Ba-133 \n Peak: 356 keV"
    textstr5 = "Element: Ba-133 \n Peak: 382 keV"
    textstr6 = "Element: Co-60 \n Peak: 1173.2 keV"
    textstr7 = "Element: Na-22 \n Peak: 511 keV"

    ax1.annotate(textstr1, xy=(75, 27), xytext=(75, 200),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr3, xy=(302, 103), xytext=(302, 25),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr4, xy=(356, 123), xytext=(500, 100),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr5, xy=(382, 133), xytext=(800, 200),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr2, xy=(1769.7, 639), xytext=(1200, 639),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr6, xy=(1170, 424), xytext=(1400, 339),arrowprops=dict(arrowstyle="->"))
    ax1.annotate(textstr7, xy=(511, 177), xytext=(370, 300),arrowprops=dict(arrowstyle="->"))
    ax1.legend(loc='lower right')
    ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
            verticalalignment='top')
    ax1.set_xlim(E.min()-25,E.max()+25)

    plt.savefig('calib.png')
    plt.show()

print(1/pf1[0], (pferr1[0]/pf1[0])*(1/pf1[0]),1/pf1[1],(pferr1[1]/pf1[1])*(1/pf1[1]))
