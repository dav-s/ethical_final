#!/usr/bin/env python3
import sys, os
from subprocess import run

lines = [line.rstrip('\n') for line in open('config.txt')]
for line in lines:
    run("wifite -e " + line)
    
