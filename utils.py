import matplotlib.pyplot as plt
import numpy as np


def histogram(data=None, x_label: str = "", y_label: str = "", title: str = "", bins=None, counter=0):
    if data is None:
        data = []
    if bins is None:
        bins = 10

    total = np.sum(data)
    samples = len(data)
    min = np.min(data)
    max = np.max(data)
    average = np.average(data)
    median = np.median(data)
    std = np.std(data)
    textstr = 'Total Sum=%.2f\n' \
              'N Samples=%d\n' \
              'Min=%.2f\n' \
              'Max=%.2f\n' \
              'Average=%.2f\n' \
              'Median=%.2f\n' \
              'Std Deviation=%.2f' % (total, samples, min, max, average, median, std)

    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(x=data, bins=bins)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_yscale('linear')
    ax.set_title(title)

    left, width = .25, .5
    bottom, height = .25, .5
    right = left + width
    top = bottom + height
    ax.text(x=right, y=top, s=textstr,
            horizontalalignment='right',
            verticalalignment='top',
            transform=ax.transAxes)

    fig.tight_layout()
    plt.show()
    plt.draw()
    fig.savefig('histogram-%d.png' % counter, dpi=200)
