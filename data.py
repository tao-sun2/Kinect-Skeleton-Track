import csv
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


def update_3d(arr):
    ax.view_init(elev=90, azim=90)
    ax.cla()
    ax.set_xlim(-1500, 1500)
    ax.set_xticks(np.arange(-1500, 1500, 500))
    ax.set_ylim(-1500, 1500)
    ax.set_yticks(np.arange(-1500, 1500, 500))
    ax.set_zlim(-5000, 5000)
    ax.set_zticks(np.arange(-5000, 5000, 500))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    pc = ax.scatter(arr[0], arr[1], arr[2], c='r')
    return pc


if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    file_name = 'test6'
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    arr = []
    lines = data.readlines()
    i = 0
    while (i + 10 <= len(lines)):
        line = lines[i]
        frame = []
        x = []
        y = []
        z = []
        if line[0] == 'S':
            body_number = int(lines[i + 2][0])
            if body_number == 0:
                i = i + 3
            else:
                i = i + 3
                if body_number >= 2:
                    print(body_number)
                for j in range(body_number):
                    i = i + 1
                    for k in range(32):
                        line = lines[i].strip().split(',')
                        x.append(float(line[0]))
                        y.append(float(line[1]))
                        z.append(float(line[2]))
                        i = i + 1
        frame.append(x[0:32])
        frame.append(y[0:32])
        frame.append(z[0:32])
        arr.append(frame)

    print(len(arr))
    arr = arr[100:len(arr)]

    ani = animation.FuncAnimation(fig=fig, func=update_3d, frames=arr, interval=50)
    plt.show()
    ani.save(file_name + "_xzy.gif")
