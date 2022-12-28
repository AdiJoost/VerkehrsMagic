import matplotlib.pyplot as plt


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