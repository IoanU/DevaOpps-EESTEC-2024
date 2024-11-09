import os
import pandas as pd
from joblib import load
from utils import load_json, save_json
from extract_features import extract_features  # Reuse the feature extraction function

def main():
    # Load the trained model
    model_path = "/usr/src/app/source/model/trained_model.pkl"
    model = load(model_path)
    
    # Directory containing test files
    test_dir = "/home/matei/Repositories/DevaOpps/InputData/test"
    predictions = {}

    # Process and classify each test file
    for filename in os.listdir(test_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(test_dir, filename)
            
            # Extract features for the test file
            features = extract_features(file_path)
            features_df = pd.DataFrame([features])  # Convert to DataFrame for model input

            # Predict label and store result
            predicted_label = model.predict(features_df)[0]
            predictions[filename] = int(predicted_label)  # Convert to int for JSON serialization

    # Save predictions to the output JSON file
    output_path = "/usr/src/app/output/labels.json"
    save_json(predictions, output_path)
    print(f"Classification complete. Predictions saved to {output_path}")

if __name__ == "__main__":
    main()

