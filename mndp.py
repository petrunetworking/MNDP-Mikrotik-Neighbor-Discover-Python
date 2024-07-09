# mndp.py
from datetime import timedelta
import struct
import socket
import time

# Define constants for MMDPType
MMDPTypeMACAddress = 1
MMDPTypeIdentity = 5
MMDPTypeVersion = 7
MMDPTypePlatform = 8
MMDPTypeUptime = 10
MMDPTypeSoftwareID = 11
MMDPTypeBoard = 12
MMDPTypeUnpack = 14
MMDPTypeIPv6Address = 15
MMDPTypeInterfaceName = 16
MMDPTypeIPv4Address = 17

# Define MMDPPart class
class MMDPPart:
    def __init__(self, type, value):
        self.type = type
        self.value = value

# Define MMDPPacket class
class MMDPPacket:
    def __init__(self, seq_no, parts):
        self.seq_no = seq_no
        self.parts = parts

# Define MMDPTLVType class
class MMDPTLVType:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

# Define String method for MMDPTLVType
def MMDPTLVType_String(t):
    if t == MMDPTypeMACAddress:
        return "MACAddress"
    elif t == MMDPTypeIdentity:
        return "Identity"
    elif t == MMDPTypeVersion:
        return "Version"
    elif t == MMDPTypePlatform:
        return "Platform"
    elif t == MMDPTypeUptime:
        return "Uptime"
    elif t == MMDPTypeSoftwareID:
        return "SoftwareID"
    elif t == MMDPTypeBoard:
        return "Board"
    elif t == MMDPTypeUnpack:
        return "Unpack"
    elif t == MMDPTypeIPv6Address:
        return "IPv6Address"
    elif t == MMDPTypeInterfaceName:
        return "InterfaceName"
    elif t == MMDPTypeIPv4Address:
        return "IPv4Address"
    else:
        return f"Unknown-{t}"

# Define DecodePacket function
def DecodePacket(contents):
    parts = []
    breader = memoryview(contents)
    
    seq_no = struct.unpack('<I', breader[:4])[0]
    breader = breader[4:]
    
    while len(breader) > 0:
        part_type = MMDPTLVType(struct.unpack('>H', breader[:2])[0])
        breader = breader[2:]
        
        contents_length = struct.unpack('>H', breader[:2])[0]
        breader = breader[2:]
        
        if part_type.value == MMDPTypeMACAddress:
            mac = breader[:contents_length]
            value = ':'.join(format(x, '02x') for x in mac)
            breader = breader[contents_length:]
        elif part_type.value in [MMDPTypeIdentity, MMDPTypeVersion, MMDPTypePlatform, MMDPTypeSoftwareID, MMDPTypeBoard, MMDPTypeInterfaceName]:
            value = breader[:contents_length].tobytes().decode('utf-8')
            breader = breader[contents_length:]
        elif part_type.value == MMDPTypeUptime:
            t = struct.unpack('<I', breader[:4])[0]
            value = timedelta(seconds=t)
            breader = breader[4:]
        elif part_type.value == MMDPTypeUnpack:
            value = breader[:contents_length].tobytes()
            breader = breader[contents_length:]
        elif part_type.value in [MMDPTypeIPv6Address, MMDPTypeIPv4Address]:
            ip = breader[:contents_length]
            value = socket.inet_ntop(socket.AF_INET6 if part_type.value == MMDPTypeIPv6Address else socket.AF_INET, ip)
            breader = breader[contents_length:]
        else:
            value = breader[:contents_length].tobytes()
            breader = breader[contents_length:]
        
        parts.append(MMDPPart(part_type, value))
    
    return MMDPPacket(seq_no, parts)

