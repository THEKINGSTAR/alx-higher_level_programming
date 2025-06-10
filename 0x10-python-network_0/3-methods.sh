#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -i -L -X OPTIONS "$1" | grep "Allow: " | sed 's/^.*: //'
