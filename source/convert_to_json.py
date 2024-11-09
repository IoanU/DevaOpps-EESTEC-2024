import os
import json
from scapy.all import rdpcap
from scapy.layers.inet import TCP

def extract_tcp_payload_to_json(pcap_path, output_json_path):
    
    # Extrage payload-ul TCP din fișierele .pcap și le salvează într-un fișier JSON.
    
    packets = rdpcap(pcap_path)
    tcp_payloads = []

    # Parcurge fiecare pachet și extrage payload-ul TCP
    for packet in packets:
        if packet.haslayer(TCP) and packet[TCP].payload:
            payload_bytes = bytes(packet[TCP].payload)
            try:
                payload_text = payload_bytes.decode("utf-8")
                tcp_payloads.append(payload_text)
            except UnicodeDecodeError:
                # Ignoră payload-urile care nu sunt în format text
                continue

    # Salvează payload-urile într-un fișier JSON
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(tcp_payloads, f, ensure_ascii=False, indent=4)

def process_pcap_files(input_dir):
    
    # Procesează toate fișierele .pcap din directorul specificat, convertindu-le în JSON și ștergând fișierele inițiale.

    for filename in os.listdir(input_dir):
        if not filename.endswith(".pcap"):
            new_filename = f"{filename}.pcap"
            new_file_path = file_path.with_name(new_filename)
            # Redenumește fișierul pentru a adăuga extensia .pcap
            file_path.rename(new_file_path)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".pcap"):
            pcap_path = os.path.join(input_dir, filename)
            json_path = os.path.join(input_dir, f"{os.path.splitext(filename)[0]}.json")

            # Extrage payload-ul și salvează în JSON
            extract_tcp_payload_to_json(pcap_path, json_path)

            # Șterge fișierul .pcap inițial
            os.remove(pcap_path)
            print(f"Fișier procesat și șters: {pcap_path}")

def main():
    # Procesează fișierele din ambele directoare
    process_pcap_files("/home/student/Desktop")
    process_pcap_files("/usr/src/app/InputData/test")

if __name__ == "__main__":
    main()
