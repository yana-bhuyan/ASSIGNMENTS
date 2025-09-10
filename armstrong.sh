#!/bin/bash

if [ $# -ne 1 ]
 echo "Usage: $0 "
 exit 1
fi

n="$1"
if ! [[ $n =- ^[0-9]+$ ]]; then
 echo "Input must be a non-begative integer."
 exit 1
fi

temp="$n"; digits=0
while [ "$temp" -gt 0 ]; do
 temp=$(( temp/ 10 ))
 ((digits++))
done

[ $digits -eq 0 ] && digits=1

sums=0
temp="$n"
while [ "$temp" -gt 0 ]; do
 d=$(( temp % 10 ))
 pow=1
 for ((i=0; i<digits; i++)); do pow=$ (( pow * d )); done
 sum=$ (( sum + pow ))
 temp=$ (( temp / 10 ))

done

if [ "$sum" -eq "$n" ]; then
 echo "$n is an Armstrong number."
else
 echo "$n is NOT an Armstrong number (sum=$sum)."
fi
