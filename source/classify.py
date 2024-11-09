import os
import pandas as pd
from joblib import load
from utils import load_json, save_json
from extract_features import extract_features

def main():
    model_path = "/home/matei/Repositories/DevaOpps/source/model/trained_model.pkl"
    columns_path = "/home/matei/Repositories/DevaOpps/source/model/feature_columns.pkl"
    test_dir = "/home/matei/Repositories/DevaOpps/InputData/test"
    output_path = "/home/matei/Repositories/DevaOpps/output/labels.json"
    predictions = {}

    # Load model and columns
    model = load(model_path)
    feature_columns = load(columns_path)
    print("Model and feature columns loaded successfully.")

    for filename in os.listdir(test_dir):
        file_path = os.path.join(test_dir, filename)
        if os.path.isfile(file_path):
            features = extract_features(file_path)
            features_df = pd.DataFrame([features])

            # Apply one-hot encoding and align columns
            features_encoded = pd.get_dummies(features_df)
            features_encoded = features_encoded.reindex(columns=feature_columns, fill_value=0)

            try:
                predicted_label = model.predict(features_encoded)[0]
                predictions[filename] = int(predicted_label)
                print(f"Prediction for {filename}: {predicted_label}")
            except Exception as e:
                print(f"Error during prediction for {filename}: {e}")
                continue

    save_json(predictions, output_path)
    print(f"Classification complete. Predictions saved to {output_path}")

if __name__ == "__main__":
    main()
