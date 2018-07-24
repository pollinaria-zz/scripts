import sys
import string

for config in sys.argv[1:]:
    project = config.split(".")[0]
    f = open(config)
    tpl = open(project + ".tpl", 'w')

    for line in f:  	
        lineBlocks = line.split(":")
        
        if lineBlocks[0].isupper():
            lineBlocks[1] = "production/config/" + project + "/" + (lineBlocks[0].lower()).strip()
            tpl.write(lineBlocks[0] + ": {{ key \"" + lineBlocks[1] +"\" }}\n")

        elif "image" in line and len(lineBlocks) == 3:
        	lineEnd = line.rfind(":")
        	tpl.write(line[:lineEnd] + ":{{ key \"production/config/" +  project + "/docker_tag\" }}\n")
        
        else:
        	tpl.write(line)


tpl.write("\n")
f.close()
tpl.close()
