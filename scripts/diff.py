#!/usr/bin/env python

import subprocess
import sys


ref_stem = sys.argv[1]
cmp_stem = sys.argv[2]
diff_bin = sys.argv[3:]

result_stdout = subprocess.run(diff_bin + [ref_stem + ".stdout.txt", cmp_stem + ".stdout.txt"])
result_stderr = subprocess.run(diff_bin + [ref_stem + ".stderr.txt", cmp_stem + ".stderr.txt"])

sys.exit(result_stdout.exitcode | result_stderr.exitcode)
