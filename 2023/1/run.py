#!/usr/bin/env python3
import re
import sys

DIGITS_MAP = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

DIGITS=list(DIGITS_MAP.keys());
DIGITS.append(r"\d")
# regex for digits
D = '|'.join(DIGITS)

RE_PATTERN = re.compile(rf"""^
                             .*?           # non-greedy everything
                            ({D})          # capture digit
                            (?:
                                   .*      # anything
                                   ({D})   # and capture digit
                                   .*      # the rest
                                |          # or
                                   .*      # no more digits
                            )
                            $""", re.VERBOSE | re.MULTILINE | re.IGNORECASE)

def get_digit(substr):
    if substr in DIGITS_MAP:
        return DIGITS_MAP[substr]
    else:
        return int(substr)

file_path = sys.argv[1]

sum = 0

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        result = RE_PATTERN.search(line)
        # when using print gives broken pipe error, why??
        if  result.group(2) is None:
            number = get_digit(result.group(1)) * 10 + get_digit(result.group(1))
        else:
            number = get_digit(result.group(1)) * 10 + get_digit(result.group(2))
        # todo other posibilities
        sum += number
print(sum)
