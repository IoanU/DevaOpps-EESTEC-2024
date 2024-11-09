import os
import json
from scapy.all import rdpcap
from pathlib import Path
from utils import load_config

# Load configuration for dynamic paths
config = load_config()

def convert_pcap_to_json(input_folder, output_folder):
    """
    Convert PCAP files in the specified folder to JSON files without changing filenames.
    """
    # Ensure the output folder exists
    output_folder.mkdir(exist_ok=True)

    # Process each PCAP file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pcap"):
            pcap_path = input_folder / filename
            packets = rdpcap(str(pcap_path))

            # Flag to indicate if a valid JSON payload was extracted
            json_extracted = False
            
            # Iterate over packets to find JSON payload
            for packet in packets:
                if packet.haslayer("TCP") and packet["TCP"].payload:
                    payload_bytes = bytes(packet["TCP"].payload)

                    try:
                        json_data = payload_bytes.decode("utf-8")
                        json_object = json.loads(json_data)

                        # Save JSON file with the same filename (no extension added)
                        json_filename = pcap_path.stem  # filename without .pcap
                        json_path = output_folder / json_filename

                        with open(json_path, "w") as json_file:
                            json.dump(json_object, json_file, indent=4)
                        
                        json_extracted = True
                        break  # Stop after extracting the first valid JSON payload

                    except (UnicodeDecodeError, json.JSONDecodeError):
                        continue

# Convert PCAP files in the train and test folders
input_folder_train = config["train_dir"]
output_folder_train = config["train_dir"]
input_folder_test = config["test_dir"]
output_folder_test = config["test_dir"]

# Run the conversions
convert_pcap_to_json(Path(input_folder_train), Path(output_folder_train))
convert_pcap_to_json(Path(input_folder_test), Path(output_folder_test))
