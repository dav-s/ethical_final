#!/usr/bin/env python3

import sys
import glob
import os
from time import sleep
from subprocess import run

if len(sys.argv) <= 1:
    print("Need to specify a dictionary file './check_bt.py <password_file>'")
    quit()

files = glob.glob(os.path.expanduser("~/Public/*.pcap"))
while len(files) == 0:
    print("Waiting for .pcap files over BlueTooth")
    sleep(5)
    files = glob.glob(os.path.expanduser("~/Public/*.pcap"))

latest_file = max(files, key=os.path.getctime)
print(f'Found file: Cracking {latest_file}')
run(f'aircrack-ng -w "{sys.argv[1]}" -l keys.txt {latest_file}', shell=True)

