#!/bin/bash
if [ -d "albums" ];
then
rm -r albums
fi
if [ -d "playlists" ];
then
rm -r playlists
fi
mkdir albums
mkdir playlists
cd songs
for x in $(ls)
do
var=$(cat $x | head -n 1)
n=$(cat $x | head -2 | tail -1)
cd ..
cd  albums
if [ ! -d "$var" ];
then
mkdir $var
fi
cd $var
ln -s ../../songs/$x $x
cd ..
cd ..
cd songs

for y in $(cat $x | tail -$n)
do
cd ..
cd playlists
if [ ! -d "$y" ];
then
mkdir $y
fi
cd $y
ln -s ../../songs/$x $x
cd ..
cd ..
cd songs
done
done
