#!/bin/bash
code=$(find . -type f -name '*.py' -exec grep -hv '#' {} +)
no_empty_lines=$(echo "$code" | grep -ve '^$')
if [ "$1" == "-v" ]; then echo "$no_empty_lines"; fi
echo "$no_empty_lines" | wc -l
