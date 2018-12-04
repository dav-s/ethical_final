#!/usr/bin/env python3
from config import *
from subprocess import run

for essid in WHITELISTED_ESSIDS:
    run(f'wifite -e "{essid}" --new-hs -i {INTERFACE}', shell=True)
