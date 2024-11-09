#!/bin/bash
# Run the feature extraction, model loading, and classification scripts in sequence

# Extract features from the training data and train the model
python3 /usr/src/app/source/train_model.py

# Classify test data using the trained model
python3 /usr/src/app/source/classify.py

# Output predictions to the expected output directory
