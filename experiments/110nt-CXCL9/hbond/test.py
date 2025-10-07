import numpy as np
import matplotlib.pyplot as plt

filename = "hbang_20ns.xvg"

# Load skipping GROMACS comments
data = np.loadtxt(filename, comments=["@", "#"])
angle_deg, prob = data[:,0], data[:,1]


plt.figure(figsize=(7,4))
plt.plot(angle_deg, prob, lw=1.2, color="#7f0000")
plt.xlabel("Hydrogen-Donor-Acceptor Angle (degrees)")
plt.ylabel("Probability")
plt.title("H-bond angle distribution")
plt.tight_layout()
plt.savefig("hbond_angle_distribution.png", dpi=300)