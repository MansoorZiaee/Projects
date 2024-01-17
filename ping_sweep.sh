#!/bin/bash

echo "Enter the Subnet"

read Subnet
#for IP1 in $(seq 16 254);do
	for IP2 in $(seq 1 254); do
		ping -c 1 $Subnet.$IP2 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> discoveredIPs.txt &
	done
#done
