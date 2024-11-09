import os
import pandas as pd
from utils import load_json

def extract_features(file_path):
    """
    Extracts relevant features from a single JSON file.
    :param file_path: Path to the JSON file.
    :return: A dictionary of extracted features.
    """
    data = load_json(file_path)
    
    features = {
        "process_name": data.get("process", {}).get("name", ""),
        "event_id": data.get("winlog", {}).get("event_id", ""),
        "event_channel": data.get("winlog", {}).get("channel", ""),
        "user_identifier": data.get("winlog", {}).get("user", {}).get("identifier", ""),
        "rule_name": data.get("rule", {}).get("name", ""),
        "log_level": data.get("log", {}).get("level", ""),
        "event_category": ','.join(data.get("event", {}).get("category", [])),
        "event_type": ','.join(data.get("event", {}).get("type", [])),
        "call_trace_length": len(data.get("winlog", {}).get("event_data", {}).get("CallTrace", "").split("|")) if "CallTrace" in data.get("winlog", {}).get("event_data", {}) else 0,
        "label": data.get("label", None)
    }
    
    return features

def main():
    train_dir = "/home/matei/Repositories/DevaOpps/InputData/train"
    output_path = os.path.join(train_dir, "train_features.csv")
    features_list = []

    # Process each file in train_dir, excluding `train_features.csv`
    for filename in os.listdir(train_dir):
        file_path = os.path.join(train_dir, filename)

        # Ensure it’s a file and not the output CSV before processing
        if os.path.isfile(file_path) and filename != "train_features.csv":
            print(f"Processing file: {filename}")
            features = extract_features(file_path)
            features_list.append(features)

    # Save extracted features to CSV
    df = pd.DataFrame(features_list)
    df.to_csv(output_path, index=False)
    print(f"Feature extraction complete. Saved to {output_path}. DataFrame saved with {len(df)} rows.")

if __name__ == "__main__":
    main()

