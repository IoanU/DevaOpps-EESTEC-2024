#!/bin/bash

# Step 0: Extract TCP payload from all test and training pcap files and convert to json files by decoding bytes
python3 ./source/convert_to_json.py

# New files are stored in folders: /InputData/test.json and /InputData/train.json

# Step 1: Extract features from training data
python3 ./source/extract_features.py

# Step 2: Train the model using the extracted features
python3 ./source/train_model.py

# Step 3: Classify test data using the trained model
python3 ./source/classify.py
