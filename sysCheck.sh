#!/bin/bash

# System Check Script

# Check Disk Usage
df -h

# Check Avaible Memory 
free -h

# Check Network Connectivity
ping -c 4 google.com
