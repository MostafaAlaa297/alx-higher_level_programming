#!/bin/bash
# Take a URL and send GET request with custom header
curl -s -H "X-School-User-Id: 98" $1
