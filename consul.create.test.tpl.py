import subprocess
import sys
import string

for config in sys.argv[1:]:
    cmd =  'consul-template -template \"' + config + ':' + config.split(".")[0] + '.ConsulTest' +'\" -once'
    subprocess.call(cmd, shell = True)
