import numpy as np
import matplotlib.pyplot as plt

r = np.loadtxt('PrecioCalidad.csv', delimiter = ",")
precios = r[:,0]
c_1 = np.zeros((10,51))
for j in range(len(c_1)):
    for i in range(len(r[0])):
        if i < len(c_1[0]):
            
            c_1[j,i] = r[j,i+1]
        else:
            break
for i in range(len(c_1[0])):
    plt.figure()
    plt.scatter(precios, c_1[:,i])
