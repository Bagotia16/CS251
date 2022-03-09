#!/bin/bash
if [ $# != 2 ]; 
then
echo "Wrong number of arguments, expected 2"
exit 1
fi
a=$1
b=$2
c=$((a+b))
echo $c
exit 0