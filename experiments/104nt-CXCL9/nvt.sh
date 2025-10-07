#!/bin/bash
#SBATCH -N 1
#SBATCH --mem=50G
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1
#SBATCH --reservation=mkoziarski_gpu
#SBATCH --time=8:00:00
#SBATCH --job-name=nvt_run
#SBATCH --out=experiments/%x-%j.out


echo "--------------------"
echo "Job started on $(date)"
echo "--------------------"


source $HOME/.bashrc
conda activate gromacs

echo $(pwd)

gmx mdrun -v -deffnm nvt


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
