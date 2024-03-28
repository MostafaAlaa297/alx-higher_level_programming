#!/bin/bash
# Take URL as input
if [ $(curl -sL -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi
