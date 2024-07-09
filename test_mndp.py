# test_mndp.py

import socket
from mndp import DecodePacket, MMDPTLVType_String

# Define the port to listen on
UDP_PORT = 5678

# Set up the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

print(f"Listening on port {UDP_PORT}...")

while True:
    # Receive data from the socket
    data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received packet from {addr}")

    # Decode the packet
    packet = DecodePacket(data)

    # Print the packet sequence number
    print(f"Sequence Number: {packet.seq_no}")

    # Print each part in the packet
    for part in packet.parts:
        part_type_str = MMDPTLVType_String(part.type.value)
        print(f"Type: {part_type_str}, Value: {part.value}")
