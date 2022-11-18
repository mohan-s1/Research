import numpy as np
import pandas as pd
import scipy.constants

hbar = 1
m = 1833.15038419  # mass of a proton in au
kb = 0.000003167  # boltzmann in au
a0 = 1  # bohr radius
lx = 1.89000189  # one angstrom in au
pi = scipy.constants.pi
nx = 10

def PIB(xpoints, xmax, xmin, mass, hbar=1):  # removing xlength for xmax + xmin
	dx = (xmax-xmin)/(xpoints-1)
	dx2 = dx**2  # second derivative
	H = np.zeros((xpoints, xpoints))
	z = -pi**2/3.0  # weight for diagonal
	for i in range(xpoints):
		for j in range(xpoints):
			if i == j:
				H[i][j] = z
			else:
				H[i][j] = (2/(i-j)**2)*((-1)**(i-j+1))  # weights for non-diagonals
	H *= (-hbar/(2*mass*dx2))
	eigvals, eigvecs = np.linalg.eigh(H)
	eigvals_list = eigvals.tolist()
	eigvals_j = eigvals*(4.3597*10**-18)  # converting the eigenvalues into joules
	eigvals_j_list = eigvals_j.tolist() # The following lines of code (28-44) are just to make exporting to excel easier
	mass_list = [mass]
	xpoints_list = [xpoints]
	xmax_list = [xmax]
	xmin_list = [xmin]
	for i in range(xpoints):
		mass_list.append(mass)
	mass_list.pop(-1)
	for i in range(xpoints):
		xpoints_list.append(xpoints)
	xpoints_list.pop(-1)
	for i in range(xpoints):
		xmax_list.append(xmax)
	xmax_list.pop(-1)
	for i in range(xpoints):
		xmin_list.append(xmin)
	xmin_list.pop(-1)
	# easist to populate using a dictionary where the pair is a list
	data = {'Mass': mass_list, 'Number of X Points': xpoints_list, 'X Max': xmax_list, 'X Min': xmin_list, 'Eigenvalues [Ha]':eigvals_list, 'Eigenvalues [J]': eigvals_j_list}
	# necessary to export to excel workbook
	df = pd.DataFrame(data) 
	# appends existing workbook by adding new sheets; flags error if sheet already exists
	with pd.ExcelWriter('/Users/mohan/Desktop/UVA/Research/one_dim_pib.xlsx', mode = "a", engine = "openpyxl") as writer:
		df.to_excel(writer, sheet_name = 'Sheet 2')
	return eigvals_j
a = PIB(nx, lx, 0, m, 1)
print(a)
