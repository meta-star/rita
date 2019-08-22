#!/usr/bin/env python3
# coding=UTF-8
"""
    Rita

        a natural language calculator

            https://project.starinc.xyz/rl

                            - A Star Inc. Research Project
        ===

    :license GPL v3.0
    :copyright 2019 Star Inc.(https://starinc.xyz) All Rights Reserved.
"""

import sys
from ritaCore import ritaCore

def main(msgs):
    result = readCommandLine(msgs)
    print(ritaCore().cal(result))

def readCommandLine(msgs):
    replymsg = ""
    for msg in msgs:
        replymsg = replymsg + " " + msg
    return replymsg

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])