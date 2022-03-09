#!/bin/bash
if [ $# -lt 1 ];
then
echo " Usage: ./cipher.sh <url> "
exit 1
fi
touch encrypted.txt
> encrypted.txt
wget -q -O encrypted.txt $1
var=$( tail -n 2 encrypted.txt )
#echo $var
my_array=($( echo $var | grep -oE '[a-zA-Z]{5}' ))
# echo ${my_array[0]}
newtext=
for x in "${my_array[@]}"
do
	y=$(echo $x | tr '[A-Z]' '[a-z]')
	first=$(echo $y | head -c 1)
	#echo $first
	rot=$(($(printf "%d" "'q") - $(printf "%d" "'$first")))
	#echo $rot
	dual=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
	dual2=ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
	newphrase=$( echo $y | tr "${dual:26:26}" "${dual:$((26+$rot)):26}")
	if [ $newphrase == queen ];
	then
		newtext=$( cat encrypted.txt | tr "${dual:26:26}" "${dual:$((26+$rot)):26}" | tr "${dual2:26:26}" "${dual2:$((26+$rot)):26}")
		break
	fi
done

echo "$newtext" > deciphered.txt

if [ -z "$newtext" ];
then
my_array=($( echo $var | grep -oE '[a-zA-Z]{7}' ))
# echo ${my_array[0]}
for x in "${my_array[@]}"
do
	y=$(echo $x | tr '[A-Z]' '[a-z]')
	first=$(echo $y | head -c 1)
	#echo $first
	rot=$(($(printf "%d" "'m") - $(printf "%d" "'$first")))
	#echo $rot
	dual=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
	dual2=ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
	newphrase=$( echo $y | tr "${dual:26:26}" "${dual:$((26+$rot)):26}")
	if [ $newphrase == majesty ];
	then
		newtext=$( cat encrypted.txt | tr "${dual:26:26}" "${dual:$((26+$rot)):26}" | tr "${dual2:26:26}" "${dual2:$((26+$rot)):26}")
		break
	fi
done
if [ ! -z "$newtext" ];
then
echo "$newtext" > deciphered.txt
fi
fi

text="PS. Give me the names."
newvar=$( echo $text | tr "${dual:26:26}" "${dual:$((26-$rot)):26}" | tr "${dual2:26:26}" "${dual2:$((26-$rot)):26}")
#echo $rot
echo "$newvar" >> encrypted.txt
exit 0