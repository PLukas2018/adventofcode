#!/usr/bin/env python3
import re
import sys

RE_PATTERN = re.compile(r"""^
                            [^\d]*        # no digit
                            (\d)          # capture digit
                            (?:
                                   .*     # anything
                                   (\d)   # and capture digit
                                   [^\d]* # followed by non-digit
                                |         # or
                                   [^\d]* # no more digits
                            )
                            $""", re.VERBOSE | re.MULTILINE)

file_path = sys.argv[1]

sum = 0

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        result = RE_PATTERN.search(line)
        if  result.group(2) is None:
            number = int(result.group(1)) * 10 + int(result.group(1))
        else:
            number = int(result.group(1)) * 10 + int(result.group(2))
        print(line, number)
        # todo other posibilities
        sum += number
print(sum)
