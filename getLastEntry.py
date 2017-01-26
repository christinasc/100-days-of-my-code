from __future__ import print_function
from subprocess import call
import os, argparse, re, time
from sys import argv

def main():
    headFile =""
    with open("log.md") as f:
        headFile = (f.read(200))        
    dayNumber = re.search(r"Day [0-9][0-9]:", headFile)
    if dayNumber:
        dayString = str(dayNumber.group(0))
        dayArray = dayString.split()
        dayNum = dayArray[1].split(':')
        count = int(dayNum[0])
        count = count +1
        print(" Matches:", dayNum[0], count)
    else: 
        print(" no match ")

if __name__ == '__main__':
    main()

