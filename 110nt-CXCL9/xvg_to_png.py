import sys
import os
import matplotlib.pyplot as plt

def read_xvg(filename):
    """Read xvg file, skipping comments/metadata lines."""
    x, y = [], []
    with open(filename) as f:
        for line in f:
            if line.startswith(('#', '@')):
                continue
            parts = line.split()
            if len(parts) >= 2:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
    return x, y

def main():
    if len(sys.argv) != 2:
        print("Usage: python plot_xvg.py <file.xvg>")
        sys.exit(1)

    infile = sys.argv[1]
    if not os.path.isfile(infile):
        print(f"Error: file '{infile}' not found")
        sys.exit(1)

    x, y = read_xvg(infile)
    if not x:
        print("No data found in file (check format).")
        sys.exit(1)

    # Convert ps→ns if times are large
    x_label = "Time (ps)"
    if max(x) > 1000:
        x = [xi / 1000 for xi in x]
        x_label = "Time (ns)"

    plt.figure(figsize=(6,4))
    plt.plot(x, y, label=os.path.basename(infile).replace(".xvg", ""))
    plt.xlabel(x_label)
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()

    outfile = "plots/" + os.path.splitext(infile)[0] + ".png"
    plt.savefig(outfile, dpi=300)
    print(f"Saved plot to {outfile}")

if __name__ == "__main__":
    main()
