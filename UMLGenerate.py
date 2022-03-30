from ast import alias
from plantweb.render import render_file
from os.path import exists
import base64

def decodeUML(svgLoc):
    encoded = base64.b64encode(open(svgLoc,'rb').read()) 
    return 'data:image/svg+xml;base64,{}'.format(encoded.decode()) 


def generateUML(CAPfilename, outputFileName, paks, aliases):
    CONTENT = ""
    #for alias in aliases:

    svgName = outputFileName.split(".")[0] +".svg"
    if exists(svgName): # check if output exist, won't generate new one
        return decodeUML(svgName)

    for pak in paks:
        for ip, alias  in aliases.items():

            if ip == pak[1]:
                src = alias
            if ip == pak[2]:
                dst = alias
        if pak[3].isnumeric():
            CONTENT += "autonumber "+pak[0] +' "<font color=green><b>Message 0  "\n'            
        else:
            CONTENT += "autonumber "+pak[0] +'\n'
            
        CONTENT+= src + " -> " + dst + " : " + pak[3] + ' [[ link {1111} info]]' +'\n'
    
    infile = outputFileName.split(".")[0] + '.dot'
    with open(infile, 'wb') as fd:
        fd.write(CONTENT.encode('utf-8'))

    outfile = render_file(
        infile,
        svgName,
        renderopts={
            'engine': 'plantuml',
            'format': 'svg'
        },
        cacheopts={
            'use_cache': False
        }
    )

    return decodeUML(svgName)