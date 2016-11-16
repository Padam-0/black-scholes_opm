import matplotlib.pyplot as plt
import random

def plot_w(list, w_list):
    change = []
    for i in range(1, len(list)):
        change.append(list[i] / list[i - 1])

    plt.plot(w_list)
    plt.plot(change)
    plt.show()


def op_w(list, w):
    change = list[-1] / list[-2]
    prev_change = (list[-2] / list[-3])
    if change > prev_change:
        return w
    else:
        m = (random.randint(0,1) * 2 - 1)
        i = w + 0.05 * m
        if i > 1 and i < 1.5:
            return i
        else:
            return w + 0.05 * (-1 * m)