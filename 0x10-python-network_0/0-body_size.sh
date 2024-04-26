#!/bin/bash
# Print a Bash script for takes in a URL
curl -s "$1" | wc -c
