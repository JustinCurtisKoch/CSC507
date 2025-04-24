#!/bin/bash

# Output log file
OUTPUT_FILE="system_monitor.log"

# Collect system metrics
SYSINFO=$(iostat | awk 'NR==1 {print "OS:", $1, $2, "VM NAME:", $3, "ARCHITECTURE:", $5}') # Basics
PROC=$(lscpu | awk 'NR==8 {print $5, $6, $3, $4, $7, $9}') # Processor info
MEMORY=$(free -h | awk 'NR==2 {print "TOTAl:", $2, "USED:", $3, "FREE:", $4}') # RAM info
STORAGE=$(df -h | awk 'NR==2 {print "SIZE:", $2, "USED:", $3, "AVAILABLE:", $4}')
IOSTATS=$(iostat | awk 'NR==4 {print "AVG CPU by USER:", $1 "%", "SYSTEM:", $3 "%", "IDLE:", $6 "%"}')
TOP_PROCESSES=$(ps -eo pid,comm,%mem,%cpu --sort=-%cpu | head -n 6) # Top 5 processes

# Write metrics to log file
{
	echo "System Monitoring Report - $(date)"
	echo "---------------------------------"
	echo "General Info $SYSINFO"
	echo "Processor: $PROC"
	echo "RAM $MEMORY"
	echo "STORAGE $STORAGE"
	echo "I/O Statistics $IOSTATS"
	echo ""
	echo "Top 5 Processes by CPU Usage:"
	echo "$TOP_PROCESSES"
	echo "---------------------------------"
} >> $OUTPUT_FILE

# Display the report on the terminal
echo "System Monitoring Report - $(date)"
echo "---------------------------------"
echo "General Info $SYSINFO"
echo "Processor: $PROC"
echo "RAM $MEMORY"
echo "STORAGE $STORAGE"
echo "I/O Statistics $IOSTATS"
echo ""
echo "Top 5 Processes by CPU Usage:"
echo "$TOP_PROCESSES"
echo "---------------------------------"
