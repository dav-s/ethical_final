#!/usr/bin/env python3
from config import *
from subprocess import run
import os

TSHARK_COMMAND = 'tshark -2 -R "eapol || wlan.fc.type_subtype == 0x04 || wlan.fc.type_subtype == 0x08" -r {} -w {} -F libpcap'

for f in os.listdir("hs"):
    if f.endswith(".cap"):
        run(TSHARK_COMMAND.format("hs/" + f, "hs/" + f[:-3] + "pcap"), shell=True)

run(f'obexftp -b {BT_MAC} -p hs/*.pcap', shell=True)
