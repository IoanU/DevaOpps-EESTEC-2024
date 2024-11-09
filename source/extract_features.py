from utils import load_json
import pandas as pd
import os

def extract_features(file_path):
    # Define feature extraction logic here
    data = load_json(file_path)
    features = {
        "process_name": data.get("process", {}).get("name", ""),
        "process_id": data.get("process", {}).get("pid", ""),
        "process_path": data.get("process", {}).get("executable", ""),
        "parent_process_id": data.get("process", {}).get("parent", {}).get("pid", ""),
        "parent_process_name": data.get("process", {}).get("parent", {}).get("name", ""),
        "parent_process_path": data.get("process", {}).get("parent", {}).get("executable", ""),
        
        "event_id": data.get("winlog", {}).get("event_id", ""),
        "event_channel": data.get("winlog", {}).get("channel", ""),
        "event_provider": data.get("winlog", {}).get("provider_name", ""),
        "event_provider_guid": data.get("winlog", {}).get("provider_guid", ""),
        "event_opcode": data.get("winlog", {}).get("opcode", ""),
        "event_task": data.get("winlog", {}).get("task", ""),
        "event_version": data.get("winlog", {}).get("version", ""),
        "event_keywords": data.get("winlog", {}).get("keywords", ""),
        
        "user_identifier": data.get("winlog", {}).get("user", {}).get("identifier", ""),
        "user_name": data.get("winlog", {}).get("user", {}).get("name", ""),
        "user_domain": data.get("winlog", {}).get("user", {}).get("domain", ""),
        "user_type": data.get("winlog", {}).get("user", {}).get("type", ""),
        
        "rule_name": data.get("rule", {}).get("name", ""),
        
        "log_level": data.get("log", {}).get("level", ""),
        
        "event_category": ','.join(data.get("event", {}).get("category", [])),
        "event_type": ','.join(data.get("event", {}).get("type", [])),
        
        "call_trace": data.get("winlog", {}).get("event_data", {}).get("CallTrace", ""),
        "call_trace_length": len(data.get("winlog", {}).get("event_data", {}).get("CallTrace", [])),
        
        "target_object": data.get("winlog", {}).get("event_data", {}).get("TargetObject", ""),
        "target_process_id": data.get("winlog", {}).get("event_data", {}).get("TargetProcessId", ""),
        "target_process_guid": data.get("winlog", {}).get("event_data", {}).get("TargetProcessGUID", ""),
        "target_process_path": data.get("winlog", {}).get("event_data", {}).get("TargetImage", ""),
        "target_user": data.get("winlog", {}).get("event_data", {}).get("TargetUser", ""),
        
        "source_process_guid": data.get("winlog", {}).get("event_data", {}).get("SourceProcessGUID", ""),
        "source_process_id": data.get("winlog", {}).get("event_data", {}).get("SourceProcessId", ""),
        "source_process_name": data.get("winlog", {}).get("event_data", {}).get("SourceImage", ""),
        "source_thread_id": data.get("winlog", {}).get("event_data", {}).get("SourceThreadId", ""),
        "source_user": data.get("winlog", {}).get("event_data", {}).get("SourceUser", ""),
        
        "granted_access": data.get("winlog", {}).get("event_data", {}).get("GrantedAccess", ""),
        "access_mask": data.get("winlog", {}).get("event_data", {}).get("AccessMask", ""),
        
        "network_protocol": data.get("winlog", {}).get("event_data", {}).get("Protocol", ""),
        "network_source_ip": data.get("winlog", {}).get("event_data", {}).get("SourceIp", ""),
        "network_source_port": data.get("winlog", {}).get("event_data", {}).get("SourcePort", ""),
        "network_destination_ip": data.get("winlog", {}).get("event_data", {}).get("DestinationIp", ""),
        "network_destination_port": data.get("winlog", {}).get("event_data", {}).get("DestinationPort", ""),
        
        "label": data.get("label", None)
    }
    return features

def main():
    train_dir = "/usr/src/app/InputData/train"
    output_path = "/usr/src/app/InputData/train/train_features.csv"
    features_list = []

    for filename in os.listdir(train_dir):
        file_path = os.path.join(train_dir, filename)
        if file_path.is_file() and filename != "train_features.csv":
            features = extract_features(file_path)
            features_list.append(features)

    df = pd.DataFrame(features_list)
    df.to_csv(output_path, index=False)
    print(f"Feature extraction complete. Saved to {output_path}. DataFrame saved with {len(df)} rows.")

if __name__ == "__main__":
    main()
