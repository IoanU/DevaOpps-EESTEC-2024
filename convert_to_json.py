from scapy.all import rdpcap # //////////////// schimbare from
import json

# Încarcă fișierul PCAP
packets = rdpcap("input.pcap") # /////////////// input.pcap fiind fisierul input

# Parcurge pachetele pentru a găsi payload-ul TCP cu date JSON
for packet in packets:
    # Verifică dacă pachetul are un strat TCP și conține payload
    if packet.haslayer("TCP") and packet["TCP"].payload:
        payload_bytes = bytes(packet["TCP"].payload) # Extrage payload-ul TCP sub forma de bytes
        
        try:
            json_data = payload_bytes.decode("utf-8") # Decodează payload-ul în UTF-8
            json_object = json.loads(json_data) # Verificare structură JSON
            
            with open("event.json", "w") as json_file:
                json.dump(json_object, json_file, indent=4) # Salvează datele JSON într-un singur fișier

            break  # Ieși din buclă după găsirea evenimentului JSON

        except (UnicodeDecodeError, json.JSONDecodeError):
            print("Payload-ul nu este JSON valid.")

# //////////////// Payload-ul JSON a fost extras și salvat în 'event.json'
