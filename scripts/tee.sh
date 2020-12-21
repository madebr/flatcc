#!/bin/bash

outputfile="$1"
shift
args=("$@")

"${args[@]}" 1>"$outputfile.stdout.txt" 2>"$outputfile.stderr.txt"
res=$?

cat "$outputfile.stdout.txt"
cat "$outputfile.stderr.txt" >&2
exit $?
