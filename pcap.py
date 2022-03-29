import sys
import pyshark
import UMLGenerate
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
     
                    if hasattr(pak.http2, "headers_status"):
                        method = pak.http2.headers_status

                    if "GET" in pak.http2.header:
                        if "nf-instances" in str(pak.http2):
                            method = "GET"

                    if "PATCH" in pak.http2.header:
                        #id = str(pak.http2).split("nf-instances/")[1].split("\n")[0]
                        method = "PATCH"

                    if "PUT" in pak.http2.header:
                        id = str(pak.http2).split("nf-instances/")[1].split("\n")[0]
                        method = "PUT"

                    if "POST" in pak.http2.header:
                        method = "POST"

                    if "DELETE" in pak.http2.header:
                        method = "DELETE"

                    if method != "":
                        data.append([pak.frame_info.number,
                                pak.ip.src,
                                pak.ip.dst,
                                method,
                                pak.http2.header])
        return data        

if __name__ == "__main__":
    
    if len(sys.argv) >1:
        jsonConfig = json.load(open(sys.argv[1])) 
    else:
        jsonConfig = json.load(open("scenarios/data.json"))

    pcapFileName = jsonConfig["pcap"]
    filters = jsonConfig["filters"]
    decodes = jsonConfig["decodes"]
    aliases = jsonConfig["aliases"]
    capObj = cap(pcapFileName)

    filteredData = capObj.check_communication(filters, decodes)

    UMLGenerate.generateUML(capObj.filename, filteredData, aliases)
    