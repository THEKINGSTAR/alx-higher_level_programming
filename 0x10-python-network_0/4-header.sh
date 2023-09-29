#!/bin/bash
# Bash script takes in a URL as argument,sends a GET request to the URL,displays the body of the response
curl -s "$1/X-School-User-Id=98" | grep "body"
