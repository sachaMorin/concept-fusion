#!/bin/bash


# Parameters
#SBATCH --job-name=concept-fusion
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ARRAY_TASKS,FAIL,TIME_LIMIT
#SBATCH --mem=16G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=1-00:00:00
#SBATCH --partition=long
#SBATCH -o /network/scratch/s/sacha.morin/logs/concept-fusion/slurm-%j.out  # Write the log on scratch


DATASET_NAME=$1
DATA_DIR=$2
SEQUENCE=$3

FT_DIR=/tmp/saved-feat # Where to save features
MAP_DIR=/tmp/saved-map # Where to save maps
FINAL_DIR=$SCRATCH/openlex-results/concept-fusion/$DATASET_NAME/$SEQUENCE # Where to save final results

SAM_CHECKPOINT_PATH=$HOME/concept-fusion/checkpoints/sam_vit_h_4b8939.pth

module load python/3.10
source $HOME/concept-fusion/venv/bin/activate

cd $HOME/concept-fusion/concept-fusion/examples

python3 extract_conceptfusion_features.py --dataset_name $DATASET_NAME --data_dir $DATA_DIR  --sequence $SEQUENCE --checkpoint_path $SAM_CHECKPOINT_PATH --save-dir $FT_DIR
python3 run_feature_fusion_and_save_map.py --dataset_name $DATASET_NAME --data_dir $DATA_DIR  --sequence $SEQUENCE --feat_dir $FT_DIR --dir_to_save_map $MAP_DIR

mkdir -p $FINAL_DIR
python3 to_openlex_format.py --cf_path $MAP_DIR --openlex_path $FINAL_DIR