# Python - Network #0

Bash scripts exploring HTTP and cURL: URLs, requests, responses, headers,
methods, status codes and POST parameters.

## Tasks

| File | Description |
|------|-------------|
| 0-body_size.sh | Displays the size (in bytes) of the response body for a URL |
| 1-body.sh | Sends a GET request and displays the body only for a 200 status code |
| 2-delete.sh | Sends a DELETE request to a URL and displays the body |
| 3-methods.sh | Displays all HTTP methods the server accepts |
| 4-header.sh | Sends a GET request with header X-HolbertonSchool-User-Id: 98 |
| 5-post_params.sh | Sends a POST request with email and subject variables |

## Usage

    ./0-body_size.sh 0.0.0.0:5000
    ./1-body.sh 0.0.0.0:5000/route_1
    ./2-delete.sh 0.0.0.0:5000/route_3
    ./3-methods.sh 0.0.0.0:5000/route_4
    ./4-header.sh 0.0.0.0:5000/route_5
    ./5-post_params.sh 0.0.0.0:5000/route_6

All scripts are 3 lines long, executable, and use curl -s.
