#!/bin/bash
# Take URL as input and send POST request with parameters
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
