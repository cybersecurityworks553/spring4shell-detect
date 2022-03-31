# Spring4Shell Detection Script
Scanner to detect the Spring4Shell vulnerability on input URLs

## Prerequisite's
- python3
- python3 -m pip install -r Requirements.txt

## Usage
python3 detect.py --help

```
usage: detect.py [-h] [--url TARGET] [--file TARGETS]

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  File containing Form Endpoints
  --url URL    target Form Endpoints
```

## Example: 1
Run the script for single URL to detect Spring4Shell Vulnerability
```
python3 detect.py --url http://192.168.0.1/greeting
```

## Example: 2
Run the script for Multiple URLs by providing text file with ips to detect Spring4Shell Vulnerability
```
python3 detect.py --file ips.txt
```

## Sample Testing
We have a Sample Spring Application set up -

Running the script against it -
```
python3 detect.py --url http://192.168.0.1/greeting
```
Output -


