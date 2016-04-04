from urllib.request import urlopen
import numpy as np

filename = input()
f = urlopen(filename)
mat = np.loadtxt(f, skiprows=1, delimiter=",")
print(mat.mean(axis=0))