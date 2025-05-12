#!/bin/bash

input_file="sh-CSC507-Mod2-PM.txt"
output_file="sh-CSC507-Mod4-PM.txt"

START=$SECONDS

while read -r number
do
	let "number *=2"
	echo $number>> $output_file
	done < $input_file

ELAPSED=$(($SECONDS - $START))
echo "$(($ELAPSED/60)) minutes $(($ELAPSED%60)) seconds"