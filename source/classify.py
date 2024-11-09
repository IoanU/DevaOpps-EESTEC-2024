from utils import load_config, load_json, save_json
import pandas as pd
import os
from joblib import load

def is_utf8(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False


def extract_features(file_path):
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
    }
    return features

def main():
    config = load_config()
    model_path = config["model_dir"] / "trained_model.pkl"
    columns_path = config["model_dir"] / "feature_columns.pkl"
    test_dir = config["test_dir"]
    output_path = config["output_dir"] / "labels"
    predictions = {}

    model = load(model_path)
    feature_columns = load(columns_path)

    for filename in os.listdir(test_dir):
        file_path = test_dir / filename
        if file_path.is_file() and is_utf8(file_path) :
            features = extract_features(file_path)
            features_df = pd.DataFrame([features])
            features_encoded = pd.get_dummies(features_df).reindex(columns=feature_columns, fill_value=0)
            try:
                predicted_label = model.predict(features_encoded)[0]
                predictions[filename] = int(predicted_label)
                #print(f"Prediction for {filename}: {predicted_label}")
            except Exception as e:
                print(f"Error during prediction for {filename}: {e}")
                continue

    save_json(predictions, output_path)
    print(f"Classification complete. Predictions saved to {output_path}")

if __name__ == "__main__":
    main()
