#!/usr/bin/env python3

import sys, os
import re # regular expressions
import csv # csv parsing
from subprocess import run

# config
PREFIX = "abc" # for file output purposes
AIRODUMP_TIMEOUT = 10

# aircrack-ng commands
AIRMON = "airmon-ng start wlan0"
AIRODUMP_BROAD = "timeout {} airodump-ng wlan0mon -o csv -w {}".format(AIRODUMP_TIMEOUT, PREFIX)
AIRODUMP_BSSID = "timeout {} airodump-ng --bssid {} -w {} wlan0mon".format((AIRODUMP_TIMEOUT, "{}", PREFIX)


# returns a list of WPA2 networks in form {ESSID, BSSID}
# expects at least one airodump CSV file with PREFIX, chooses the latest
def fetch_wpa2_networks_from_csv():
    networks = []

    prefixed_files = list(filter(lambda x: PREFIX in x, os.listdir()))]

    try:
        highest_number = max([int(re.findall("{}-(\d+).csv".format(PREFIX), x)[0]) for x in prefixed_files])
    except(ValueError):
        print("Error: Could not find CSV files with prefix:'{}'.".format(PREFIX))

    latest_csv = "{}-{}.csv".format(PREFIX, highest_number)

    with open(latest_csv) as csv_file:
        csv_file_reader = csv.DictReader(csv_file)
        for row in csv_file_reader:
            # break once we get to the 2nd part of the csv, we dont care about it
            if ("Station MAC" in row["BSSID"]):
                break

            if "WPA2" in row[" Privacy"]: # could be " WPA2" or " WPA2 WPA"
                networks.append({"ESSID":row[" ESSID"], # note: it's " ESSID", with a space
                            "BSSID":row["BSSID"]})
    return networks



def main():

    # enable monitor mode on wlan0
    run(AIRMON.split())

    # fetch networks from airodump, retry if none are found
    network = []
    while not network:
        run(AIRODUMP.split(), timeout=AIRODUMP_TIMEOUT)
        network = fetch_wpa2_networks_from_csv()

    # TODO:
        # AIRODUMP_BSSID on each BSSID
        # DEAUTH client MAC addresses found
        # capture reauthentication 


if __name__ == '__main__':
    main()
