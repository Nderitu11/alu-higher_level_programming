#!/bin/bash
# Displays the size in bytes of the body of the response for a given URL
curl -s "$1" | wc -c
