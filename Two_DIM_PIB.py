import numpy as np
import matplotlib.pyplot as plt
import scipy.constants

hbar = 1
m = 1833.15038419  # mass of a proton in au
kb = 0.000003167  # boltzmann in au
a0 = 1  # bohr radius
lx = 1.89000189  # one angstrom in au
ly = 1.89000189  # one angstrom in au
pi = scipy.constants.pi
nx = 10
ny = 10

def PIB_TWO(xpoints, xmax, xmin, ypoints, ymax, ymin, mass, hbar=1):
    dx = (xmax-xmin)/(xpoints-1) 
    dx2 = dx**2
    dy = (ymax-ymin)/(ypoints-1)
    dy2 = dy**2
    H = np.zeros((xpoints*ypoints, xpoints*ypoints))
    i = -1 # first index used to describe for the Hamiltonian matrix
    for i1 in range(xpoints):
        for i2 in range(ypoints):
            i = i+1
            j = -1 # second index used to describe Hamiltonian matrix
            for j1 in range(xpoints):
                for j2 in range(ypoints):
                    j = j+1
                    if i2 == j2:
                        if i1 == j1:
                            z = -pi**2/3.0
                        else:
                            z = (2/(i1-j1)**2)*((-1)**(i1-j1+1))
                        z = -1*z*hbar**2 / (2.0 * m * dx2)
                        H[i][j] = H[i][j] + z
                    if i1 == j1:
                        if i2 == j2:
                            zz = -pi**2/3.0
                        else:
                            zz = (2/(i2-j2)**2)*((-1)**(i2-j2+1))
                        zz = -1*z*hbar**2 / (2.0 * m* dy2)
                        H[i][j] = H[i][j] + zz
    eigvals, eigvecs = np.linalg.eigh(H)
    eigvals_j = eigvals*(4.3597*10**-18)
    return eigvals
a = PIB_TWO(nx, lx, 0, ny, ly, 0, m, 1)
print(a)
