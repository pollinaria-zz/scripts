  GNU nano 2.5.3                                                            File: consul.kv.py                                                                                                                      Modified  

import sys
import consul
import string

c = consul.Consul()

for config in sys.argv[1:]:
    consulDict = {}
    project = config.split(".")[0]
    consulDir = 'production/config/'+ project + "/"
    c.kv.put(consulDir, None)
    f = open(config)
    for line in f:
        lineBlocks = line.split(":")
        if lineBlocks[0].isupper():
           lineValue = line.find(":") + 2
           consulDict[(consulDir + (lineBlocks[0].lower()).strip())] = line[lineValue:].rstrip()

        elif "image" in line and len(lineBlocks) == 3:
                lineEnd = (line.rfind(":") + 1)
                consulDict[consulDir + "docker_tag"] = line[lineEnd:].rstrip()

    for k in consulDict:
        v = consulDict[k]
        c.kv.put(k, v)
