from utils import load_config, load_json
import pandas as pd
import os

def is_utf8(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False

def extract_features(file_path):
    # Define feature extraction logic here
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
        "call_trace_length": len(data.get("winlog", {}).get("event_data", {}).get("CallTrace", [])),
        "label": data.get("label", None)
    }
    return features

def main():
    config = load_config()
    train_dir = config["train_dir"]
    output_path = train_dir / "train_features.csv"
    features_list = []

    for filename in os.listdir(train_dir):
        file_path = train_dir / filename
        if file_path.is_file() and is_utf8(file_path) and filename != "train_features.csv":
            features = extract_features(file_path)
            features_list.append(features)

    df = pd.DataFrame(features_list)
    df.to_csv(output_path, index=False)
    print(f"Feature extraction complete. Saved to {output_path}. DataFrame saved with {len(df)} rows.")

if __name__ == "__main__":
    main()
