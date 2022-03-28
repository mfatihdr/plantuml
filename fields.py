CAP_FILENAME = "assets/pcaps/STOAMF1Pcap17001.pcap"

decodeAs = {
    'tcp.port==8001':'http2',
    'tcp.port==8005':'http2',
    'tcp.port==8006':'http2',
    'tcp.port==8007':'http2',
    'tcp.port==8009':'http2',
    'tcp.port==8010':'http2'
}

dFilter = "tcp.port == 53494 or tcp.port == 34784 or tcp.port == 40192 or tcp.port == 53498"

aliases = [
    ["10.10.33.84_53494", "nf1"],
    ["10.10.33.81_8001", "nf2"],
    ["10.10.33.84_34784", "nf3"],
    ["10.10.33.81_8006", "nf4"],
    ["10.10.33.84_53498", "nf5"],
    ["10.10.33.84_40192", "nf6"],
    ["10.10.33.81_8007", "nf7"]
]