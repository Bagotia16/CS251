import os
import argparse
from argparse import ArgumentParser

parser = ArgumentParser(description="canonical path")
parser.add_argument("-inp", dest="inp", required=True,
    help="input file with arbitrary path", metavar="FILE")
parser.add_argument("-out", dest="out", required=True,
    help="output file where canonical path is stored", metavar="FILE")
args = parser.parse_args()

f1=open(args.inp,"r")
s=f1.readline()
# print(s[-1])
var=os.path.realpath(s[:-1])

f2=open(args.out,"w")
f2.write(var)
f2.close()
f1.close()