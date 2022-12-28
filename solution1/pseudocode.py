import matplotlib.pyplot as plt
from plots.logger import Logger
import os


def showMagic(leftTraffic, rightTraffic):
    plt.subplot(1,2,1)
    plt.xlabel('Cells')
    plt.ylabel('Timesteps')
    plt.title("Left Lane")
    plt.imshow(leftTraffic, cmap='Blues')
    plt.subplot(1,2,2)
    plt.title("Right Lane")
    plt.xlabel('Cells')
    plt.imshow(rightTraffic, cmap='Reds')
    plt.show()

def saveMagic(leftTraffic, rightTraffic, street, name):
    plt.subplot(1,2,1)
    plt.xlabel('Cells')
    plt.ylabel('Timesteps')
    plt.title("Left Lane")
    plt.imshow(leftTraffic, cmap='Blues')
    plt.subplot(1,2,2)
    plt.title("Right Lane")
    plt.xlabel('Cells')
    plt.imshow(rightTraffic, cmap='Reds')
    my_path = os.getcwd().split("VerkehrsMagic", 1)[0]
    my_path = os.path.join(my_path, "VerkehrsMagic", "solution1", "plots", name)
    plt.savefig(my_path)
    dataPoints = (
        name,
        street.gridsize,
        street.dally,
        street.spawnRate,
        street.tunnel,
        street.maxSpeed,
        street.tunnelSpeedLimit
    )
    Logger.log_csv(dataPoints, "metaData")

