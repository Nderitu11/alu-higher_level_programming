#!/bin/bash
# Send a GET request to the URL with header X-HolbertonSchool-User-Id set to 98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
