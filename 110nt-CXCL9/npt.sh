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

gmx grompp -f npt.mdp -c nvt.gro -t nvt.cpt -r nvt.gro -p topol.top -n prot_dna_index.ndx -o npt.tpr

gmx mdrun -v -deffnm npt


# sbatch ~/andrew/md/110nt-CXCL9/md.sh


echo "--------------------"
echo "Job ended on $(date)"
echo "--------------------"
