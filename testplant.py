from plantweb.render import render
from plantweb.render import render_file

from pcap import cap


def generateUML(paks, aliases):
    CONTENT = ""
    #for alias in aliases:
    for pak in paks:
        for ip, alias in aliases:
            if ip == pak[1]:
                src = alias
            if ip == pak[2]:
                dst = alias
        if pak[3] == "200 OK" or pak[3] == "201 Created":
            CONTENT+= "autonumber "+pak[0] +' "<font color=green><b>Message 0  "\n'
        else:
            CONTENT+= "autonumber "+pak[0] +'\n'
            
        CONTENT+= src + " -> " + dst + " : " + pak[3] + " [[ link {This is a tip} info]]" +'\n'
    return CONTENT
    

if __name__ == '__main__':

    ### pcap sec. start
    CAP_FILENAME = "STOAMF1Pcap17001.pcap"
    
    
    decodeAs = {
        'tcp.port==8001':'http2',
        'tcp.port==8005':'http2',
        'tcp.port==8006':'http2',
        'tcp.port==8007':'http2',
        'tcp.port==8009':'http2',
        'tcp.port==8010':'http2'
    }
    
    
    dFilter = "tcp.port == 53494 or tcp.port == 34784 or tcp.port == 40192 or tcp.port == 53498"
    #dFilter = ""

    c = cap(CAP_FILENAME)

    data_pak = c.check_communication(dFilter, decodeAs)
    ### pcap sec. fin

    # set nf for each src/dst
    aliases = [
        ["10.10.33.84_53494", "nf1"],
        ["10.10.33.81_8001", "nf2"],
        ["10.10.33.84_34784", "nf3"],
        ["10.10.33.81_8006", "nf4"],
        ["10.10.33.84_53498", "nf5"],
        ["10.10.33.84_40192", "nf6"],
        ["10.10.33.81_8007", "nf7"]
    ]
    cont = generateUML(data_pak, aliases)

    infile = 'mygraph.dot'
    with open(infile, 'wb') as fd:
        fd.write(cont.encode('utf-8'))

    outfile = render_file(
        infile,
        renderopts={
            'engine': 'plantuml',
            'format': 'svg'
        },
        cacheopts={
            'use_cache': False
        }
    )
