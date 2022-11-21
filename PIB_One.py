import numpy as np
import pandas as pd
import scipy.constants
import matplotlib.pyplot as plt

h = scipy.constants.h
hbar = 1
m = 1833.15038419  # mass of a proton in au
kb = 0.000003167  # boltzmann in au
a0 = 1  # bohr radius
lx = 1.89000189  # one angstrom in au
pi = scipy.constants.pi
nx = 5
lx_meters = 1*10**-10
m_kg = 1.67*10**-27

def PIB(xpoints, xmax_au, xmin_au, mass_au, mass_kg, length_m, hbar=1,):  # removing xlength for xmax + xmin
    dx = (xmax_au-xmin_au)/(xpoints-1)
    dx2 = dx**2  # second derivative
    H = np.zeros((xpoints, xpoints))
    z = -pi**2/3.0  # weight for diagonal
    for i in range(xpoints):
        for j in range(xpoints):
            if i == j:
                H[i][j] = z
            else:
                H[i][j] = (2/(i-j)**2)*((-1)**(i-j+1))  # weights for non-diagonals based on 'distance' from point
    H *= (-hbar/(2*mass_au*dx2))
    eigvals, eigvecs = np.linalg.eigh(H)
    eigvals_list = eigvals.tolist()
    eigvals_j = eigvals*(4.3597*10**-18)  # converting the eigenvalues into joules
    eigvals_j_list = eigvals_j.tolist() # Line 33-55 make are so exporting data into excel runs better
    mass_au_list = []
    xpoints_list = []
    xmax_au_list = []
    xmin_au_list = []
    mass_kg_list = []
    length_m_list = []
    correct_eigvals = []
    for i in range(xpoints):
        mass_au_list.append(mass_au)
    for i in range(xpoints):
        xpoints_list.append(i)
    for i in range(xpoints):
        xmax_au_list.append(xmax_au)
    for i in range(xpoints):
        xmin_au_list.append(xmin_au)
    for i in range(xpoints):
        mass_kg_list.append(mass_kg)
    for i in range(xpoints):
        length_m_list.append(length_m)
    for i in range(xpoints):
        correct = ((h**2*(i+1)**2)/(8*m_kg*lx_meters**2))
        correct_eigvals.append(correct)
    # easist to populate using a dictionary where the pair is a list
    data = {'Mass [au]': mass_au_list, 'Mass [kg]': mass_kg_list, 'Number of X Points': xpoints_list, 'X Max [au]': xmax_au_list, 'X Min [au]': xmin_au_list, 'Eigenvalues [Ha]': eigvals_list, 'Eigenvalues [J]': eigvals_j_list, 'Analytical Eigenvalues [J]': correct_eigvals}
    # necessary to export to excel workbook
    df = pd.DataFrame(data) 
    # appends existing workbook by adding new sheets; flags error if sheet already exists
    with pd.ExcelWriter('/Users/mohan/Desktop/UVA/Research/one_dim_pib.xlsx', mode = "a", engine = "openpyxl") as writer:
        df.to_excel(writer, sheet_name = 'Sheet 8')
    return 
