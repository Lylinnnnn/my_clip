#!/bin/bash

python -m training.main \
    --save-frequency 10 \
    --train-data "/home/radiance/ego4d_dealt_data/medium_train_output_0104.csv" \
    --val-data "/home/radiance/ego4d_dealt_data/medium_test_output_0104.csv" \
    --dataset-type "csv" \
    --batch-size 64 \
    --workers 8 \
    --lr 2e-4 \
    --wd 0.001 \
    --epochs 10 \
    --warmup 500 \
    --model ViT-B-32 \
    --force-image-size 224 \
    --report-to "tensorboard" \
    --log-every-n-steps 1000 \
    --lr-scheduler const
