#!/bin/bash

DATASET_NAME=replica
DATA_DIR=$SCRATCH/data/Replica

for sequence in room0 room1 room2 office0 office1 office2 office3 office4
do 
    sbatch $HOME/concept-fusion/concept-fusion/slurm/full_conceptfusion.sh $DATASET_NAME $DATA_DIR $sequence
done
