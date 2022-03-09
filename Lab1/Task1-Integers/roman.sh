#!/bin/bash
N=$1
while [ $N -gt 0 ]
do
if [ $N -ge 100 ]
then
printf C
((N-=100))
elif [ $N -ge 90 ]
then
printf XC
((N-=90))
elif [ $N -ge 50 ]
then
printf L
((N-=50))
elif [ $N -ge 40 ]
then
printf XL
((N-=40))
elif [ $N -ge 10 ]
then
printf X
((N-=10))
elif [ $N -ge 9 ]
then
printf IX
((N-=9))
elif [ $N -ge 5 ]
then
printf V
((N-=5))
elif [ $N -ge 4 ]
then
printf IV
((N-=4))
else
printf I
((N-=1))
fi
done