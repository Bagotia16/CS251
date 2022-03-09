#!/bin/bash
if [ $# -lt 1 ];
then
echo "No numbers given"
exit 1
fi
sum=0
for a in "$@"
do
sum=$((sum+a))
done
echo $sum
exit 0