#!/usr/bin/python

import urllib
import os.path

def urlquote(infile, outfile):
    for line in infile.readlines():
        outfile.write(urllib.quote(line.strip()) + '\n')

def urlunquote(infile, outfile):
    for line in infile.readlines():
        outfile.write(urllib.unquote(line.strip()) + '\n')

import sys
if __name__ == '__main__':
    basename = os.path.basename(sys.argv[0])
    infile = sys.stdin
    outfile = sys.stdout
    if basename == 'urlquote':
        urlquote(infile, outfile)
    elif basename == 'urlunquote':
        urlunquote(infile, outfile)

