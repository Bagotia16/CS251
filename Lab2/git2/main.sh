#! /bin/bash

md1=$(cat binaries/dep1 | md5sum | awk -F ' ' '{print $1}')
md2=$(cat binaries/dep2 | md5sum | awk -F ' ' '{print $1}')
md3=$(cat binaries/dep3 | md5sum | awk -F ' ' '{print $1}')
md4=$(cat binaries/dep4 | md5sum | awk -F ' ' '{print $1}')
md5=$(cat binaries/dep5 | md5sum | awk -F ' ' '{print $1}')

_md1="48db4582bb48e597e122011b44443f77"
_md2="84a4082251391920ea825976197f46dc"
_md3="a14af954df74dae9a9bdcb9b7a6e6774"
_md4="53445b1475cbe1b8a684b253302272fe"
_md5="550e58b4a27a1ce02f1ef8a5b95f4d32"


if [ $md1 = $_md1 ] && [ $md2 = $_md2 ] && [ $md3 = $_md3 ] && [ $md4 = $_md4 ] && [ $md5 = $_md5 ]; then
	echo "Everything is fine :)"
else
	echo "Something is wrong :("
fi


