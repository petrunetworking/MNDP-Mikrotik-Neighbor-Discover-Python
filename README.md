# MNDP Mikrotik Neighbor Discover-Python
This repository contains Python code to decode Mikrotik Network Discovery Protocol (MNDP) packets. It includes a script to listen for MNDP packets on a specific UDP port (5678) and decode them for analysis.

## Contents

- `mndp.py`: Contains the MNDP packet decoding functionality.
- `listen_mndp_packets.py`: Script to listen for MNDP packets on UDP port 5678, decode them, and print the results.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/petrunetworking/MNDP-Mikrotik-Neighbor-Discover-Python.git
    cd MNDP-Mikrotik-Neighbor-Discover-Python
    ```

2. (Optional) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install any required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the Decoder**

   Ensure `mndp.py` contains the necessary code for decoding MNDP packets.

2. **Run the Listener Script**

   Run `python listen_mndp_packets.py` to start listening for MNDP packets on UDP port 5678:
    ```sh
    python3 listen_mndp_packets.py # for linux
    ```

   The script will output the decoded packet details.

## Example
```python  listen_mndp_packets.py
Listening on port 5678...
Received packet from ('10.20.30.3', 5678)
Sequence Number: 4
Type: MACAddress, Value: 00:15:5d:9b:84:0a
Type: Identity, Value: MikroTik
Type: Version, Value: 6.49.15 (stable)
Type: Platform, Value: MikroTik
Type: Uptime, Value: 1:48:04
Type: SoftwareID, Value: KWgrt3zzfbC
Type: Board, Value: CHR
Type: Unpack, Value: b'\x00'
Type: InterfaceName, Value: ether1
Type: IPv4Address, Value: 10.20.30.3

Received packet from ('10.20.30.2', 5678)
Sequence Number: 534
Type: MACAddress, Value: 00:15:5d:9b:84:06
Type: Identity, Value: MikroTik_234576_SCP
Type: Version, Value: 6.49.15 (stable)
Type: Platform, Value: MikroTik
Type: Uptime, Value: 4:50:09
Type: SoftwareID, Value: rGNFINCEloH
Type: Board, Value: CHR
Type: Unpack, Value: b'\x00'
Type: InterfaceName, Value: ether1
Type: IPv4Address, Value: 10.20.30.2

Received packet from ('10.20.30.3', 5678)
Sequence Number: 5
Type: MACAddress, Value: 00:15:5d:9b:84:0a
Type: Identity, Value: MikroTik
Type: Version, Value: 6.49.15 (stable)
Type: Platform, Value: MikroTik
Type: Uptime, Value: 1:49:04
Type: SoftwareID, Value: KWgrt3zzfbC
Type: Board, Value: CHR
Type: Unpack, Value: b'\x00'
Type: InterfaceName, Value: ether1
Type: IPv4Address, Value: 10.20.30.3

Received packet from ('10.20.30.2', 5678)
Sequence Number: 535
Type: MACAddress, Value: 00:15:5d:9b:84:06
Type: Identity, Value: MikroTik_234576_SCP
Type: Version, Value: 6.49.15 (stable)
Type: Platform, Value: MikroTik
Type: Uptime, Value: 4:51:09
Type: SoftwareID, Value: rGNFINCEloH
Type: Board, Value: CHR
Type: Unpack, Value: b'\x00'
Type: InterfaceName, Value: ether1
Type: IPv4Address, Value: 10.20.30.2```
![image](https://github.com/petrunetworking/MNDP-Mikrotik-Neighbor-Discover-Python/assets/126423814/0ccf0365-d4cc-47ce-bbe9-fd8520af2d8e)
