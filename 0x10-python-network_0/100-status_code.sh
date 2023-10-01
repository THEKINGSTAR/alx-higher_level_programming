#!/bin/bash
#Bash script sends request to URL passed as an argument, displays only the status code of the response.
curl -s -w "%{http_code}" "$1" | tail -c 3
