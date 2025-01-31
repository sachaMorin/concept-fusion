#!/bin/bash

DATASET_NAME=scannetpp
DATA_DIR=$SCRATCH/data/scannetpp_openlex_v2

for sequence in 0a76e06478  0a7cc12c0e  1f7cbbdde1  410c470782  49a82360aa  4c5c60fa76  8a35ef3cfe  c0f5742640  d918af9c5f  fd361ab85f
do 
    sbatch $HOME/concept-fusion/concept-fusion/slurm/full_conceptfusion.sh $DATASET_NAME $DATA_DIR $sequence
done
