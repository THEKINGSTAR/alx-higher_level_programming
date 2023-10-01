#!/bin/bash
#Bash script sends a DELETE request to URL passed as the first argument and displays the body of the response
curl -X DELETE "$1"
