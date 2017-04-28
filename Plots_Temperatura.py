import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1 ,100)

x, y = np.meshgrid(x,y)

for caso in range(1,3):
    if(caso==1):
        cas="SinFuente"
    elif(caso ==2):
        cas="ConFuente"
    for condicion in range(1, 4):
        if(condicion == 1):
            con="Libre"
        elif (condicion ==2):
            con = "Periodicas"
        else:
            con = "Fijas"
        inicio = "Tpromedio"
        fin1 = ".txt"
        fin2 = ".png"
        filename1= inicio+cas+con+fin1
        tprom = np.loadtxt(filename1)

        filename2= inicio+cas+con+fin2

        plt.figure()
        plt.plot(tprom[:,0],tprom[:,1])
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Temperatura Promedio [C]")
        plt.title(inicio+cas+con)
        plt.savefig(filename2)
        plt.close()

        inicio = "TPlaca"
        tiempo = "0"
        filename3= inicio+cas+con+tiempo+fin1
        filename4= inicio+cas+con+tiempo+fin2
        temp = np.loadtxt(filename3)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(x, y, temp, cmap=cm.coolwarm)
        ax.set_xlabel("X [m]")
        ax.set_ylabel("Y [m]")
        ax.set_zlabel("Temperatura [C]")
        ax.set_title(inicio+cas+con+tiempo)
        plt.savefig(filename4)
        plt.close()

        tiempo = "100"
        filename3= inicio+cas+con+tiempo+fin1
        filename4= inicio+cas+con+tiempo+fin2
        temp = np.loadtxt(filename3)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(x, y, temp, cmap=cm.coolwarm)
        ax.set_xlabel("X [m]")
        ax.set_ylabel("Y [m]")
        ax.set_zlabel("Temperatura [C]")
        ax.set_title(inicio+cas+con+tiempo)
        plt.savefig(filename4)
        plt.close()

        tiempo = "2500"
        filename3= inicio+cas+con+tiempo+fin1
        filename4= inicio+cas+con+tiempo+fin2
        temp = np.loadtxt(filename3)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(x, y, temp, cmap=cm.coolwarm)
        ax.set_xlabel("X [m]")
        ax.set_ylabel("Y [m]")
        ax.set_zlabel("Temperatura [C]")
        ax.set_title(inicio+cas+con+tiempo)
        plt.savefig(filename4)
        plt.close()
