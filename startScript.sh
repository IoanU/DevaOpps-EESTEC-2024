#!/bin/bash

# Step 1: Extract features from training data
python3 ./source/extract_features.py

# Step 2: Train the model using the extracted features
python3 ./source/train_model.py

# Step 3: Classify test data using the trained model
python3 ./source/classify.py

