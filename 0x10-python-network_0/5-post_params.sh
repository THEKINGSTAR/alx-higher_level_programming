#!/bin/bash
email='test@gmail.com' subject='I will always be here for PLD'
curl -s -X POST  -d "email=$email&subject=$subject" "$1"
