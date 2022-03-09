#!/bin/bash
wget -q -r -np -R "index.html*" $2 					#download all files

FILE_NAME=$2
FILE_NAME=$(echo $FILE_NAME | cut -c 9-)			# FILE_NAME is now without https://

mkdir ./verifier

cp -r ./"$FILE_NAME"inputs/ ./verifier/
cp -r ./"$FILE_NAME"outputs/ ./verifier/            #copy input and output folders only
FILE_NAME=${FILE_NAME%%/*}
rm -r $FILE_NAME

cp $1 ./											#copy the code

mkdir ./verifier/my_outputs/

echo "Failed testcases are:" > ./feedback.txt		#start feedback.txt

i=0

CODE=$( basename $1 )
g++ $CODE 											#run the code

for INPUTS in ./verifier/inputs/* ; 				#iterate overall input files
do
	EXTN=`echo "$INPUTS" | cut -d'.' -f3`
	if [ "$EXTN" == "in" ]
	then 
		./a.out <$INPUTS> $i.out
		mv $i.out ./verifier/my_outputs/$i.out 		#store outpot in .out files and move them
	fi 												#to the my_outputs folder
	((i+=1))
done

((i--)) 											#due to last unintentional assignment


j=0													#j is to keep track of no of correct outputs
k=0 												#and k is to store in feedback.txt
for OUTPUTS in ./verifier/outputs/* ;
do
	OUT=$( basename $OUTPUTS )
	MY_OUT_NAME=$( cat $OUTPUTS )
	MY_OUT=$( cat ./verifier/my_outputs/$OUT )
	if [ "$MY_OUT_NAME" == "$MY_OUT" ]
	then
		((j++))
		((k++))
	else
		echo $k >> feedback.txt
		((k++))
	fi
done

if [ "$j" == "$i" ]									#if no. of correct test cases equal original
then 												#test cases we are good, else print failed.
	echo "All testcases passed!"
else
	echo "Some testcases failed."
fi