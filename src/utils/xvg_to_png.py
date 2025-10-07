import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import argparse


def parse_xvg_metadata(filename):
    """Extract title and axis labels from XVG file header."""
    title = None
    xlabel = None
    ylabel = None
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('@    title'):
                # Extract text between quotes
                title = line.split('"')[1] if '"' in line else None
            elif line.startswith('@    xaxis  label'):
                xlabel = line.split('"')[1] if '"' in line else None
            elif line.startswith('@    yaxis  label'):
                ylabel = line.split('"')[1] if '"' in line else None
            elif line.startswith('@TYPE') or (not line.startswith('#') and not line.startswith('@')):
                # Stop when we reach the data section
                break
    
    return title, xlabel, ylabel


def plot_xvg(filename, transparent=False):
    input_path = Path(filename)
    
    # Parse metadata from XVG file
    title, xlabel, ylabel = parse_xvg_metadata(input_path)
    
    # Load skipping GROMACS comments
    data = np.loadtxt(input_path, comments=["@", "#"])
    angle_deg, prob = data[:, 0], data[:, 1]

    plt.figure(figsize=(7,4))
    plt.plot(angle_deg, prob, lw=1.2, color="#7f0000")
    plt.xlabel(xlabel if xlabel else "X-axis")
    plt.ylabel(ylabel if ylabel else "Y-axis")
    plt.title(title if title else "Plot")
    plt.tight_layout()

    if transparent:
        output_path = input_path.with_name(f"{input_path.stem}_transparent.png")
        plt.savefig(output_path, dpi=300, transparent=True)
    else:
        output_path = input_path.with_name(f"{input_path.stem}.png")
        plt.savefig(output_path, dpi=300)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert XVG files to PNG plots')
    parser.add_argument('file', type=str, help='Input XVG file path')
    parser.add_argument('--transparent', action='store_true', 
                        help='Save plot with transparent background')
    
    args = parser.parse_args()
    plot_xvg(args.file, args.transparent)