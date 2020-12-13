#!/bin/bash
#SBATCH --time=1:00:00
#SBATCH --mem=4GB
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --job-name=Kfold_cross_validation 
#SBATCH --output=HW_sm8847_KFold_%A_%a.txt



# Usage: 
# sbatch --array=3,5,10 HW5_SM8847_ThreeTextFiles.sh
module purge
module load scikit-learn/intel/0.18.1
cd /home/sm8847
python HW5_sm8847.py $SLURM_ARRAY_TASK_ID
