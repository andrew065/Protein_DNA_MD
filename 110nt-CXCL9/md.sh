#!/bin/bash
#SBATCH -N 1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=8
#SBATCH --time=8:00:00
#SBATCH --job-name=nvt_run
#SBATCH --out=%x-%j.out


echo "--------------------"
echo "Job started on $(date)"
echo "--------------------"


module load gromacs/2024.4

gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -n prot_dna_index.ndx -o md_0_10.tpr

gmx mdrun -v -deffnm md_0_10


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
