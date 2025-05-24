#!/bin/bash

input_file="sh-CSC507-Mod2-PM.txt"
output_file="sh-CSC507-Mod4-PM.txt"

START=$SECONDS

while read -r line
do
    if [[ $line =~ ^[0-9]+$ ]]; then
        let "line *= 2"
        echo $line >> $output_file
    fi
done < $input_file

ELAPSED=$(($SECONDS - $START))
echo "$(($ELAPSED/60)) minutes $(($ELAPSED%60)) seconds"