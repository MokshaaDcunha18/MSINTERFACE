from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
from scapy.packet import Raw

# Function to process each packet
def process_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto

        print(f"Source IP: {src_ip} -> Destination IP: {dst_ip} | Protocol: {proto}")

        if Raw in packet:
            payload = packet[Raw].load
            print(f"Payload: {payload}\n")

# Start packet sniffing (Capturing the first 5 packets for demonstration)
packets = sniff(filter="ip", prn=process_packet, count=5)
