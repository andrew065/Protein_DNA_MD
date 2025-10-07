#!/bin/bash
#SBATCH -N 1
#SBATCH --mem=20G
#SBATCH --cpus-per-task=4
#SBATCH --time=24:00:00
#SBATCH --gres=gpu:1
#SBATCH --reservation=mkoziarski_gpu
#SBATCH --job-name=md_run_20ns
#SBATCH --out=%x-%j.out


echo "--------------------"
echo "Job started on $(date)"
echo "--------------------"


# module load gromacs/2024.4

source $HOME/.bashrc

conda activate gromacs

# preprocess for MD run
gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -n prot_dna_index.ndx -o md_1_20ns.tpr

# run MD simulation
gmx mdrun -v -deffnm md_1_20ns

# use instead if continuing from checkpoint
# gmx mdrun -v -deffnm md_1_100ns -cpi md_1_100ns.cpt -append


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
