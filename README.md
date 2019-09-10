# ProdPerfect Technical Evaluation
----------------------------------

## Requirements
* Python 3
* pip
* virtualenv (I mean sure, technically not a requirement, but let's not kid ourselves)

## Setup
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Exercise One
Suppose you are given a string, domain (e.g. "prodperfect.com"). Please write an application that outputs if the service at domain is responding to requests, independent of its current accessibility to you.

### Usage
```
./exercise_one.py prodperfect.com
```

## Exercise Two
Suppose you are given two files, input.txt and patterns.txt.  Please write an application that takes these files and can do the following things:

1. Output the lines in input.txt that exactly match a line in pattern.txt.
2. Output the lines in input.txt that contain a line in pattern.txt.
3. (Optional) Output the lines in input.txt that are an edit distance of 1 away from a line in pattern.txt.

