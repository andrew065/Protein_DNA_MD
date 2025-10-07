# Protein-DNA Molecular Dynamics Simulation Protocol

A comprehensive GROMACS-based workflow for performing molecular dynamics (MD) simulations on protein-DNA complexes. This protocol was developed for McMaster iGEM's REACT 2025 project focusing on CXCL9 protein-DNA aptamer interactions.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Directory Structure](#directory-structure)
- [Analysis](#analysis)
- [HPC Batch Jobs](#hpc-batch-jobs)
- [References](#references)

## Overview

This repository contains a complete MD simulation pipeline for studying protein-DNA interactions using the GROMACS molecular dynamics package with the CHARMM36 force field. 

A detailed step-by-step tutorial notebook is available at `notebooks/protein_dna_md_tutorial.ipynb` that walks through the entire workflow from PDB preprocessing to trajectory analysis.

The `experiments/` directory contains MD simulation results for three different CXCL9 protein-DNA complexes (98nt, 104nt, and 110nt aptamers), including trajectory files, analysis outputs, and visualization data.

## Requirements

### System Requirements

- **OS**: Linux (recommended for HPC clusters)
- **GROMACS**: Version 2020 or later with CUDA support
- **Python**: 3.7+
- **GPU**: NVIDIA GPU recommended (tested on L4)

### Software Dependencies

#### Core MD Software
- GROMACS (2025.3 with CUDA support)
- AmberTools 23.6

#### Python Packages
- gmx_MMPBSA (for interaction entropy analysis)
- NumPy, SciPy, Pandas
- Matplotlib (for visualization)

#### Force Field
- CHARMM36 force field (July 2022 or later)
  - Download from: [MacKerell Lab](https://mackerell.umaryland.edu/charmm_ff.shtml#gromacs)

## Installation

### Option 1: Using Conda (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/andrew065/Protein_DNA_MD.git
cd Protein_DNA_MD
```

2. Create the conda environment:
```bash
conda env create -f environment.yml
conda activate gromacs
```

### Option 2: Manual Installation

1. Install GROMACS with CUDA support:
```bash
wget http://ftp.gromacs.org/pub/gromacs/gromacs-2023.3.tar.gz
tar xfz gromacs-2023.3.tar.gz
cd gromacs-2023.3
mkdir build && cd build
cmake .. -DGMX_BUILD_OWN_FFTW=ON -DGMX_MPI=on -DGMX_GPU=CUDA
make -j 8
sudo make install
source /usr/local/gromacs/bin/GMXRC
```

2. Install Python dependencies:
```bash
pip install numpy scipy pandas matplotlib gmx_MMPBSA
```

3. Download CHARMM36 force field and place in your working directory.


## References

### Resources

1. **GROMACS**: http://manual.gromacs.org/
2. **CHARMM36 Force Field**: https://mackerell.umaryland.edu/charmm_ff.shtml
3. **GROMACS Tutorials**: http://www.mdtutorials.com/gmx/complex/
4. **gmx_MMPBSA**: https://valdes-tresanco-ms.github.io/gmx_MMPBSA/

### MDP Files

All `.mdp` files are adapted from Justin Lemkul's GROMACS tutorials:
- http://www.mdtutorials.com/gmx/complex/04_ions.html

## Contributing

This protocol is part of McMaster iGEM's REACT 2025 project. For questions or contributions:

1. Open an issue on GitHub
2. Submit a pull request with improvements
3. Contact the McMaster iGEM team

## System Information

**Test System:**
- Protein: CXCL9 (125 residues, 2,077 atoms)
- DNA: 110 nucleotides (3,501 atoms)
- Total system: ~685,000 atoms (including water and ions)
- Box type: Dodecahedron
- Water model: TIP3P
- Force field: CHARMM36

---

**Last Updated**: January 2025  
**Maintained by**: McMaster iGEM REACT 2025 Team
