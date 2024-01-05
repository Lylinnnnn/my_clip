#!/bin/bash


torchrun --nproc_per_node 2 -m training.main \
    --train-data "/home/radiance/ego4d_dealt_data/medium_train_output_0104.csv" \
    --val-data "/home/radiance/ego4d_dealt_data/medium_test_output_0104.csv" \
    --dataset-type "csv" \
    --batch-size 128 \
    --workers 32 \
    --warmup 6250 \
    --lr 0.00001 \
    --wd 0.001 \
    --epochs 10 \
    --model ViT-B-32 \
    --report-to "tensorboard" \
    --log-every-n-steps 10