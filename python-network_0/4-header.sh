#!/bin/bash
# Send a GET request to the given URL with the X-HolbertonSchool-User-Id header set to 98
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
