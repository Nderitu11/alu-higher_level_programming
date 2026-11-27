#!/usr/bin/env bash
# Sends a GET request to the given URL with header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
