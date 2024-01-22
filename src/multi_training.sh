#!/bin/bash

# ViT-S-32
# lr: 2.56e-5 / 8
# --train-data "/home/radiance/ego4d_dealt_data/medium_train_output_0104.csv" \
# --val-data "/home/radiance/ego4d_dealt_data/medium_test_output_0104.csv" \
# --lr 2e-4 \
# --warmup 500 \
export CUDA_VISIBLE_DEVICES=0,1

torchrun --nproc_per_node 2 -m training.main \
    --save-frequency 10 \
    --train-data "/home/radiance/ego4d_dealt_data/medium_train_output_0104.csv" \
    --val-data "/home/radiance/ego4d_dealt_data/medium_test_output_0104.csv" \
    --dataset-type "csv" \
    --batch-size 512 \
    --workers 8 \
    --lr 5e-4 \
    --wd 0.001 \
    --epochs 30 \
    --warmup 500 \
    --model ViT-B-32 \
    --force-image-size 224 \
    --report-to "tensorboard" \
    --log-every-n-steps 500 \
    --lr-scheduler const