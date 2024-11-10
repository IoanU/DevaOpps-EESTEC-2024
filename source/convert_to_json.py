import os
import json
from scapy.all import rdpcap
from pathlib import Path
from scapy.layers.inet import IP, TCP

def pcap_to_json(pcap_file):
    # Read packets from the pcap file
    packets = rdpcap(pcap_file)
    tcp_streams = {}

    for packet in packets:
        if IP in packet and TCP in packet and packet[TCP].payload:
            connection_id = (packet[IP].src, packet[IP].dst, packet[TCP].sport, packet[TCP].dport)
            tcp_streams.setdefault(connection_id, b"").extend(bytes(packet[TCP].payload))

    json_data = []
    for stream_data in tcp_streams.values():
        try:
            data = json.loads(stream_data.decode('utf-8'))
            json_data.append(data)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue  # Skip invalid JSON streams

    return json_data if json_data else None

def process_pcap_files(input_dir):
    
    # Procesează toate fișierele .pcap din directorul specificat, convertindu-le în JSON și ștergând fișierele inițiale.

    for filename in os.listdir(input_dir):
        file_path = Path(input_dir) / filename
        if not filename.endswith(".pcap"):
            new_filename = f"{filename}.pcap"
            new_file_path = file_path.with_name(new_filename)
            # Redenumește fișierul pentru a adăuga extensia .pcap
            file_path.rename(new_file_path)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".pcap"):
            pcap_path = os.path.join(input_dir, filename)
            json_path = os.path.join(input_dir, f"{os.path.splitext(filename)[0]}.json")

            # Extrage payload-ul si salveaza in json_path
            json_path = pcap_to_json(pcap_path)

            # Șterge fișierul .pcap inițial
            os.remove(pcap_path)
            print(f"Fișier procesat și șters: {pcap_path}")

def main():
    # Procesează fișierele din ambele directoare
    process_pcap_files("/usr/src/app/InputData/train")
    process_pcap_files("/usr/src/app/InputData/test")

if __name__ == "__main__":
    main()
