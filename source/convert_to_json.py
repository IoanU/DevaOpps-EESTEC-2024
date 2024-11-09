import os
import json
from scapy.all import rdpcap
from pathlib import Path
from utils import load_config

# Load configuration for dynamic paths
config = load_config()

# Process PCAP files for test files
input_folder_test = config["test_dir"]
output_folder_test = config["test_dir"].parent / "test.json"

# Create output folder if it doesn't already exist
output_folder_test.mkdir(exist_ok=True)

# Iterate over all files in the test input folder
for filename in os.listdir(input_folder_test):
    if filename.endswith(".pcap"):
        pcap_path = input_folder_test / filename
        packets = rdpcap(str(pcap_path))
        
        json_extracted = False  # Flag to indicate if a valid JSON payload was extracted
        
        # Iterate over packets to find JSON payload
        for packet in packets:
            if packet.haslayer("TCP") and packet["TCP"].payload:
                payload_bytes = bytes(packet["TCP"].payload)
                
                try:
                    json_data = payload_bytes.decode("utf-8")
                    json_object = json.loads(json_data)
                    
                    # Create JSON file for this PCAP file
                    json_filename = pcap_path.stem + ".json"
                    json_path = output_folder_test / json_filename
                    
                    with open(json_path, "w") as json_file:
                        json.dump(json_object, json_file, indent=4)
                    
                    json_extracted = True
                    break

                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue

# Process PCAP files for training files
input_folder_train = config["train_dir"]
output_folder_train = config["train_dir"].parent / "train.json"

# Create output folder if it doesn't already exist
output_folder_train.mkdir(exist_ok=True)

# Iterate over all files in the train input folder
for filename in os.listdir(input_folder_train):
    if filename.endswith(".pcap"):
        pcap_path = input_folder_train / filename
        packets = rdpcap(str(pcap_path))
        
        json_extracted = False  # Flag to indicate if a valid JSON payload was extracted
        
        # Iterate over packets to find JSON payload
        for packet in packets:
            if packet.haslayer("TCP") and packet["TCP"].payload:
                payload_bytes = bytes(packet["TCP"].payload)
                
                try:
                    json_data = payload_bytes.decode("utf-8")
                    json_object = json.loads(json_data)
                    
                    # Create JSON file for this PCAP file
                    json_filename = pcap_path.stem + ".json"
                    json_path = output_folder_train / json_filename
                    
                    with open(json_path, "w") as json_file:
                        json.dump(json_object, json_file, indent=4)
                    
                    json_extracted = True
                    break

                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
