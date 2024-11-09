# step 3.0

import os
import json
from scapy.all import rdpcap

# Specifică directorul de intrare cu fișiere PCAP
input_folder = "../InputData/test"
output_folder = "../InputData/test.json"

# Creează folderul de output dacă nu există deja
os.makedirs(output_folder, exist_ok=True)

# Parcurge toate fișierele din folderul de intrare
for filename in os.listdir(input_folder):
    if filename.endswith(".pcap"):
        pcap_path = os.path.join(input_folder, filename)
        packets = rdpcap(pcap_path)
        
        json_extracted = False  # Flag pentru a indica dacă a fost extras un JSON valid
        
        # Parcurge pachetele pentru a găsi payload-ul JSON
        for packet in packets:
            if packet.haslayer("TCP") and packet["TCP"].payload:
                payload_bytes = bytes(packet["TCP"].payload)
                
                try:
                    json_data = payload_bytes.decode("utf-8")
                    json_object = json.loads(json_data)
                    
                    # Creează fișierul JSON pentru acest fișier PCAP
                    json_filename = os.path.splitext(filename)[0] + ".json"
                    json_path = os.path.join(output_folder, json_filename)
                    
                    with open(json_path, "w") as json_file:
                        json.dump(json_object, json_file, indent=4)
                    
                    # print(f"Payload-ul JSON a fost extras și salvat în '{json_filename}'")
                    json_extracted = True
                    break

                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
        
        # Dacă nu s-a găsit JSON valid, afișează un mesaj
        if not json_extracted:
            # print(f"Nu a fost găsit niciun payload JSON valid în '{filename}'")

# 'x.pcap' este transformat in 'x.json' si mutat in folderul test.json, nou creat in InputData
