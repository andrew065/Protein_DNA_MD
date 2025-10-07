import sys
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np

def plot_xvg(filename):
    # read all lines to grab headers
    with open(filename) as f:
        header = [line for line in f if line.startswith(("@", "#"))]
    data = np.loadtxt(filename, comments=["@", "#"])

    x, y = data[:,0], data[:,1]

    # decide if it's time series or histogram
    if any("Time" in line for line in header):
        x = x / 1000.0
        xlabel = "Time (ns)"
    elif any("Angle" in line for line in header):
        xlabel = "Angle (degrees)"
    elif any("Distance" in line for line in header):
        xlabel = "Distance (nm)"
    else:
        xlabel = "X"

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(filename)
    plt.title(f"H-bond analysis: {filename}")
    plt.savefig(Path(filename).with_suffix(".png"), dpi=300)
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plot_xvg.py <file.xvg>")
    else:
        plot_xvg(sys.argv[1])

