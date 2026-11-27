#!/bin/bash
# Displays all the HTTP methods the server at a given URL will accept
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f 2- | tr -d "\r"
