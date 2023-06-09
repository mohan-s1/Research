import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/home/dell/lammps/projects/likoslab/one_one_gr/oneone_new.txt', sep =' ', skiprows = 4)
r= data.iloc[0:, 1].dropna().to_numpy()
gr = data.iloc[0:, 2].dropna().to_numpy()
c3 = data.iloc[0:, 3].dropna().to_numpy()

plt.plot(r, gr)
plt.savefig('/home/dell/lammps/projects/likoslab/one_one_gr/images/myRDF_all_cutoff/time_0.0005_cutoff_2.0_run_10000.png', dpi = 700)
plt.show()
