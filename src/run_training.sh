#!/bin/bash

python -m training.main \
    --dataset-type "csv" \
    --train-data "/home/radiance/ego4d_dealt_data/small_train_output_0104.csv" \
    --val-data "/home/radiance/ego4d_dealt_data/small_test_output_0104.csv" \
    --warmup 1 \
    --batch-size 8 \
    --lr 1e-5 \
    --wd 0.1 \
    --epochs 15 \
    --workers 3 \
    --model ViT-B-32 \
    --report-to "tensorboard" \
    --log-every-n-steps 5
