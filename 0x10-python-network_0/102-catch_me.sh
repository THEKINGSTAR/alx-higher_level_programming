#!/bin/bash
# Bash script that makes a request causes the server to respond with a message containing You got me!
curl -o /dev/null -sL  -X POST "" 0.0.0.0:5000/catch_m
