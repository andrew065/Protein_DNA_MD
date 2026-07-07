# Protein-DNA Molecular Dynamics Simulation Protocol
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

3. Install Python dependencies:
```bash
pip install numpy scipy pandas matplotlib gmx_MMPBSA
```

4. Download CHARMM36 force field and place in your working directory.


### Option 2: Running the Notebook on DRAC with a Python venv

Use this option on DRAC systems where GROMACS is already provided as an HPC module. In this setup, use a Python virtual environment for the notebook and load GROMACS with `module load`; do not install or activate the conda environment.

1. Clone the repository and create a Python virtual environment:
```bash
git clone https://github.com/andrew065/Protein_DNA_MD.git
cd Protein_DNA_MD
python -m venv .venv
source .venv/bin/activate
```

2. Install the notebook Python dependencies into the venv:
```bash
pip install numpy scipy pandas matplotlib gmx_MMPBSA jupyter ipykernel
python -m ipykernel install --user --name protein-dna-md --display-name "Protein-DNA MD (venv)"
```

3. Load the DRAC GROMACS module before running the notebook or submitting jobs. The Slurm scripts in this repository use the same pattern with a simple `module load ...` line:
```bash
module load gromacs/2024.4
jupyter lab notebooks/protein_dna_md_tutorial.ipynb
```

4. If you submit the included Slurm scripts on DRAC, make sure the GROMACS module line is active and comment out the conda-specific setup lines:
```bash
module load gromacs/2024.4
# source $HOME/.bashrc
# conda activate gromacs
```

The `source $HOME/.bashrc` and `conda activate gromacs` lines are only needed for the conda environment workflow. For DRAC venv usage, keep the venv activation for notebook dependencies and rely on the loaded GROMACS module for `gmx` commands.

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
