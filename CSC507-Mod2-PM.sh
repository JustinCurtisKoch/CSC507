#!/bin/bash

OUTPUT_FILE="sh-CSC507-Mod2-PM.txt"

{
	START=$SECONDS  
	echo "PM Bash script called $(date)"
	for ((i=1; i<10; i++))
	do
		echo $RANDOM
	done
	ELAPSED=$(($SECONDS - $START))
	echo "$(($ELAPSED/60)) minutes $(($ELAPSED%60)) seconds"
} >> $OUTPUT_FILE

# 1000001