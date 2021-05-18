"""
File: VISUALIZATION.PY
Author: Patrick McNamee
Date: May 17th, 2021

Brief: Python script for creating plots that appear in the final report.
"""

from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

rc('text', usetex=True)
rc('font', size=10)
rc('legend', fontsize=10)
rc('text.latex', preamble=r'\usepackage{cmbright}')


if __name__ == "__main__":
    # Load in training history
    th = np.load("../../training-history/cnn-i2c-th.npy")

    # Get figure
    fig, ax = plt.subplots(1,1)

    # size figure
    fig.set_size_inches(3.5,2)

    # Epoch vector for plotting
    epoch_vec = np.arange(th.shape[0]) + 1

    ax.plot(
        epoch_vec, th[:,0],
        label="Training Loss",
        linewidth=3,
        color="C0",
        )
    ax.plot(
        epoch_vec, th[:,1],
        label="Validation Loss",
        linewidth=3,
        color="C1",
        )
    
    # Label axis
    ax.set_xlabel("Epochs", size=10)
    ax.set_ylabel("Bezier Loss Function", size=10)
    
    # Legend
    ax.legend(
        loc='center', bbox_to_anchor=(0.5,0.9),
        ncol=2, fontsize=10,
        handlelength=0.75, handletextpad=0.2,
        columnspacing=1
    )
    
    # Limits on the graphs
    ax.set_xlim(0, epoch_vec[-1])
    ax.set_ylim(0.1, 10)

    # Set axis scales
    ax.set_yscale("log")
    
    # Formatting ticks
    ax.xaxis.set_major_locator(ticker.MultipleLocator(9*250))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(250))
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Grid
    ax.grid(True, which='major', linestyle='-', linewidth=1)
    ax.grid(True, which='minor', linestyle='--', linewidth=1)


    # Axis positioning adjustment
    ax.set_position([0.2, 0.225, 0.75, 0.7])
    plt.savefig("cnn-i2c-th.eps", pad_inches=0)
    
    plt.show()

    # Load in training history
    th = np.load("../../training-history/cnn-i2p-th.npy")

    # Get figure
    fig, ax = plt.subplots(1,1)

    # size figure
    fig.set_size_inches(3.5,2)

    # Epoch vector for plotting
    epoch_vec = np.arange(th.shape[0]) + 1

    ax.plot(
        epoch_vec, th[:,0],
        label="Training Loss",
        linewidth=3,
        color="C0",
        )
    ax.plot(
        epoch_vec, th[:,1],
        label="Validation Loss",
        linewidth=3,
        color="C1",
        )
    
    # Label axis
    ax.set_xlabel("Epochs", size=10)
    ax.set_ylabel("Mean Squared Error", size=10)
    
    # Legend
    ax.legend(
        loc='center', bbox_to_anchor=(0.5,0.1),
        ncol=2, fontsize=10,
        handlelength=0.75, handletextpad=0.2,
        columnspacing=1
    )
    
    # Limits on the graphs
    ax.set_xlim(0, epoch_vec[-1])
    ax.set_ylim(0.0001, 2)

    # Set axis scales
    ax.set_yscale("log")
    
    # Formatting ticks
    ax.xaxis.set_major_locator(ticker.MultipleLocator(9*250))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(250))
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Grid
    ax.grid(True, which='major', linestyle='-', linewidth=1)
    ax.grid(True, which='minor', linestyle='--', linewidth=1)


    # Axis positioning adjustment
    ax.set_position([0.2, 0.225, 0.75, 0.7])
    plt.savefig("cnn-i2p-th.eps", pad_inches=0)
    
    plt.show()
