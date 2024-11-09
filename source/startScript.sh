#!/bin/bash

# Check if we're running in the task environment or locally
if [ -n "$TASK_ENVIRONMENT" ]; then
    # Task environment paths
    DATAFOLDER="/usr/src/app/DataFolder"
    INPUTDATA="/usr/src/app/InputData"
    SOURCE="/usr/src/app/source"
    OUTPUT="/usr/src/app/output"
else
    # Local environment paths (relative paths based on this script's location)
    BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd .. && pwd)"
    DATAFOLDER="$BASE_DIR/DataFolder"
    INPUTDATA="$BASE_DIR/InputData"
    SOURCE="$BASE_DIR/source"
    OUTPUT="$BASE_DIR/output"
fi

# Step 1: Install packages from DataFolder/packageScript.sh
echo "Installing packages..."
$DATAFOLDER/packageScript.sh

# Step 2: Convert PCAP files to JSON (for both training and test data)
echo "Converting PCAP files to JSON format..."
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
echo "Saving output to $OUTPUT/labels..."

echo "Pipeline completed successfully."
