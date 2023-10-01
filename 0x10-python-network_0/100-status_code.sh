#!/bin/bash
#Bash script sends request to URL passed as an argument, displays only the status code of the response.
curl -o /dev/null -s -w "%{http_code}" "$1"
