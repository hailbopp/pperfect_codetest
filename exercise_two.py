#!/usr/bin/env python3
from __future__ import print_function, unicode_literals

import sys

import Levenshtein


def find_matches(inputs_filename: str, patterns_filename: str):
    # I'm going to make possibly bad assumptions here and load patterns into memory as for performance.
    # If the patterns file is _huge_ (i.e. gigabytes), we're gonna have a problem, but that would require some serious
    # consideration.

    # I was previously compiling these into regexes and attempting to find all at once, but it was more trouble than it
    # was worth at this juncture.
    partial_matches = []
    full_matches = []
    fuzzy_matches = []

    patterns = []

    with open(patterns_filename) as handler:
        patterns = handler.readlines()

    with open(inputs_filename) as handler:
        content = [line.rstrip('\n') for line in handler]
        for line in content:
            for p in patterns:
                if p in line:
                    partial_matches.append(line)

                    if p == line:
                        full_matches.append(line)

                if Levenshtein.distance(p, line) == 1:
                    fuzzy_matches.append(line)

    print("Full line matches:")
    for m in full_matches:
        print(m)

    print("\nPartial matches:")
    for m in partial_matches:
        print(m)

    print("\nMatches with edit distance of exactly 1:")
    for m in fuzzy_matches:
        print(m)


def main(input_filename: str, patterns_filename: str):
    find_matches(input_filename, patterns_filename)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
