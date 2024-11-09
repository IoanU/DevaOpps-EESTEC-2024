#!/bin/bash

# Detect environment and set paths dynamically
DATAFOLDER="/usr/src/app/DataFolder"
INPUTDATA="/usr/src/app/InputData"
SOURCE="/usr/src/app/source"
OUTPUT="/usr/src/app/output"

# Ensure the output directory exists
mkdir -p "$OUTPUT"

# Step 1: Install packages from DataFolder/packageScript.sh
# echo "Installing packages..."
# $DATAFOLDER/packageScript.sh

# Step 2: Convert PCAP files to JSON in both train and test directories
echo "Converting PCAP files to JSON format in both train and test directories..."
python3 $SOURCE/convert_to_json.py

# Step 3: Run feature extraction on training data
echo "Extracting features from training data..."
python3 $SOURCE/extract_features.py

# Step 4: Train the model using extracted features
echo "Training the model..."
python3 $SOURCE/train_model.py

# Step 5: Classify test data
echo "Classifying test data..."
python3 $SOURCE/classify.py

# Step 6: Move the generated labels.json to the output directory with correct filename

echo "Pipeline completed successfully."
