#!/bin/bash

# ViT-S-32
# lr: 2.56e-5 / 8

export CUDA_VISIBLE_DEVICES=0,1

torchrun --nproc_per_node 2 -m training.main \
    --train-data "/root/open_clip/modified_small_test_output_0112.csv" \
    --val-data "/root/open_clip/modified_small_test_output_0112.csv" \
    --dataset-type "csv" \
    --batch-size 512 \
    --workers 24 \
    --lr 3.2e-6 \
    --wd 0.001 \
    --warmup 200 \
    --epochs 10 \
    --model ViT-B-32 \
    --force-image-size 224 \
    --report-to "tensorboard" \
    --log-every-n-steps 1000000000 \
    --lr-scheduler const
