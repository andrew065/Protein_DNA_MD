#!/bin/bash
#SBATCH -N 1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=8
#SBATCH --time=8:00:00
#SBATCH --job-name=em_run
#SBATCH --out=%x-%j.out


echo "--------------------"
echo "Job started on $(date)"
echo "--------------------"


module load gromacs/2024.4

gmx mdrun -v -deffnm em


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
