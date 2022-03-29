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

                    if hasattr(pak.http2, "headers_method"):
                        method = pak.http2.headers_method

                    if method != "":
                        data.append([
                            pak.frame_info.number,
                            pak.ip.src,
                            pak.ip.dst,
                            method,
                            pak.http2.header
                        ])
        return data        

if __name__ == "__main__":
    
    if len(sys.argv) >1:
        jsonConfig = json.load(open(sys.argv[1])) 
    else:
        jsonConfig = json.load(open("scenarios/pdu_session_kurulumu.json"))

    pcapFileName = jsonConfig["pcap"]
    filters = jsonConfig["filters"]
    decodes = jsonConfig["decodes"]
    aliases = jsonConfig["aliases"]
    capObj = cap(pcapFileName)

    filteredData = capObj.check_communication(filters, decodes)

    UMLGenerate.generateUML(capObj.filename, filteredData, aliases)
    