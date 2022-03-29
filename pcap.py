import sys
import pyshark
# import pandas as pd
import json

class cap:
    def __init__(self, filename):
        self.paks = []
        self.filename = filename

    def check_communication(self, dFilter = "", decodeAs = {}, set_params = None):
        
        self.cap = pyshark.FileCapture(self.filename, decode_as = decodeAs , display_filter= dFilter)

        data = []
        for pak in self.cap:
            method = ""
            if hasattr(pak, "http2"):

                if hasattr(pak.http2, "headers"):

                    if "GET" in pak.http2.header:
                        if "nf-instances" in str(pak.http2):
                            method = "GET"

                    if "201" in pak.http2.header and "Created" in pak.http2.header:
                        method = "201 Created"
   
                    if "200" in pak.http2.header and "OK" in pak.http2.header:
                        method = "200 OK"

                    if "PATCH" in pak.http2.header:
                        id = str(pak.http2).split("nf-instances/")[1].split("\n")[0]
                        method = "PATCH"

                    if "PUT" in pak.http2.header:
                        id = str(pak.http2).split("nf-instances/")[1].split("\n")[0]
                        method = "PUT"

                    if "POST" in pak.http2.header:
                        method = "POST"

                    if "DELETE" in pak.http2.header:
                        method = "POST"

                    if method != "":
                        data.append([pak.frame_info.number,
                                pak.ip.src+"_"+pak.tcp.srcport,
                                pak.ip.dst+"_"+pak.tcp.dstport,
                                method,
                                pak.http2.header])
        return data
        #return pd.DataFrame(data, columns=["frameID", "src", "dst", "Method", "Header"])
        

if __name__ == "__main__":
    
    jsonConfig = json.load(open(sys.argv[1])) 

    CAP_FILENAME = jsonConfig["pcap"]
    
    decodeAs = jsonConfig["decodes"]
    
    dFilter = jsonConfig["filters"]
    #dFilter = ""

    c = cap(CAP_FILENAME)

    d = c.check_communication(dFilter, decodeAs)
    
    print(d)
   #////////////////////////////////////////////////////////////
    # CAP_FILENAME = "pcap_files/STOAMF1Pcap17001.pcap"
    
    # decodeAs = {
    #     'tcp.port==8001':'http2',
    #     'tcp.port==8005':'http2',
    #     'tcp.port==8006':'http2',
    #     'tcp.port==8007':'http2',
    #     'tcp.port==8009':'http2',
    #     'tcp.port==8010':'http2'
    # }
    
    # dFilter = "tcp.port == 53494 or tcp.port == 34784 or tcp.port == 40192 or tcp.port == 53498"
    # #dFilter = ""

    # c = cap(CAP_FILENAME)

    # d = c.check_communication(dFilter, decodeAs)
   #////////////////////////////////////////////////////////////
