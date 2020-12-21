#!/bin/bash

ref_stem="$1"
shift
cmp_stem="$1"
shift

args=("$@")

"${args[@]}" "$ref_stem.stdout.txt" "$cmp_stem.stdout.txt"
res_stdout=$?

"${args[@]}" "$ref_stem.stderr.txt" "$cmp_stem.stderr.txt"
res_stderr=$?

if [[ $res_stdout -ne 0 || $res_stderr -ne 0 ]]; then
    exit 1;
fi

exit 0
