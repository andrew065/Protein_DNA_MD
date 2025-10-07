#!/bin/bash
#SBATCH -N 1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=12
#SBATCH --time=8:00:00
#SBATCH --job-name=em_run
#SBATCH --out=experiments/%x-%j.out


echo "--------------------"
echo "Job started on $(date)"
echo "--------------------"


source $HOME/.bashrc

conda activate gromacs

gmx mdrun -v -deffnm em


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
