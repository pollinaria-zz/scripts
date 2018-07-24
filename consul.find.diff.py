import subprocess
import sys
import string

for config in sys.argv[1:]:

    copy = config.split(".")[0] + '.ConsulTest'
    cmd =  'diff ' + config + ' ' + copy 
    
    subprocess.call(cmd, shell = True)
