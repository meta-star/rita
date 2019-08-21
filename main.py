#!/usr/bin/env python3
# coding=UTF-8

import sys

def main(msgs):
    result = readCommandLine(msgs)
    print(result)

def readCommandLine(msgs):
    replymsg = ""
    for msg in msgs:
        replymsg = replymsg + " " + msg
    return replymsg

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])