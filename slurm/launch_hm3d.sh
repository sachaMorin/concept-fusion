#!/bin/bash

DATASET_NAME=hm3d
DATA_DIR=$SCRATCH/data/hm3d

for sequence in 00824  00829  00843  00847  00873  00877  00890
do 
    sbatch $HOME/concept-fusion/concept-fusion/slurm/full_conceptfusion.sh $DATASET_NAME $DATA_DIR $sequence
done
