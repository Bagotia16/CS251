#!/bin/bash
a=$1
key=$2
c=$3
cd $a
touch $c
> $c	
f=($(ls))
n=${#f[@]}
for((i=0; i<$n; i++))
do
if [ $(cat ${f[i]} | head -2 | tail -1) == $key ];
then
echo $(cat ${f[i]} | head -1 | tail -1) >> $c
key=$(cat ${f[i]} | head -3 | tail -1) 
i=-1
fi
done