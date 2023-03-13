import numpy as np
import matplotlib.pyplot as plt
import math


def Temperaturefunction(N):
    l = 1                       # Length of 2D domain in meter
    T1 = 273                    # Temperature T1 for other three sides in kelvin
    T2 = 100+273                # Temperature T2 for upper side in kelvin
    Nx = 100                    # Nx gird size
    Ny = 100                    # Ny gird size
    T3 = T2-T1
    n = N                         # size N
    T = np.zeros((Nx, Ny))      # created 2D array of temeprature T
    # create an array of x values from 0 to l with Nx number of points
    x = np.linspace(0, l, Nx)
    # create an array of y values from 0 to l with Ny number of points
    y = np.linspace(0, l, Ny)
    X, Y = np.meshgrid(x, y)    # create a mesh grid of X and Y values

    # compute the temperature at each point in the grid using the given formula
    for i in range(0, Nx):
        x = l*i/Nx
        for j in range(0, Ny):
            y = l*j/Ny
            for k in range(1, n+1):
                Ln = k*math.pi/l
                T[i, j] += (2*T3/math.pi)*(((-1)**(k+1)+1)/k) * \
                    ((math.sin(Ln*x))*(math.sinh(Ln*y))/math.sinh(Ln*l))

    T = T+T1                      # add T1 to the entire array T
    # return T
    # plot the temperature distribution using contourf function from matplotlib library
    plt.contourf(Y, X, T, camp='jet', levels=100)
    plt.colorbar()
    plt.xlabel(f'y lenght of plate {l} in meter')
    plt.ylabel(f'x lenght of plate {l} in meter')
    plt.title(f'Temperature distribution in kelvin for n={n}')
    plt.show()


# call the Temperaturefunction with different values of N and print the output
print(Temperaturefunction(100), Temperaturefunction(120))
