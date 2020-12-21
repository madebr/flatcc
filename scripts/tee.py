#!/usr/bin/env python

import subprocess
import sys

outputfile = sys.argv[1]
exec_cmd = sys.argv[2:]
proc = subprocess.Popen(exec_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
sys.stdout.write(stdout)
sys.stderr.write(stderr)
with open(outputfile + ".stderr.txt", "w") as ferr:
    ferr.write(stderr)
with open(outputfile + ".stdout.txt", "w") as fout:
    fout.write(stdout)
sys.exit(proc.returncode)
