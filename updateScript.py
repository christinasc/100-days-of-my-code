'''
This is a quick and dirty script to make it more efficient to update my log
file for the 100days of code challenge. Got tired of repeatedly typing, so condensed
the following commands to one call to this script - python updateScript.py 

requires python 2.7.10. 

for virtual env setup , requires 'source env/bin/activate'

git checkout log.md
emacs -nw log.md
git commit -m "today'supdate" log.md
git push

'''

from __future__ import print_function
from subprocess import call
import os, argparse, re, time
from sys import argv


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def main():
    linebreak = "----------------------------"
    preamble = "# 100 Days Of Code - Log "
    dateline = "### Day "
    progressline = "**Today's Progress**:"

    call(["ls", "-l"])
    call(["git", "status"])
    call(["git", "checkout", "log.md"])
    print(linebreak)

    now = time.strftime("%c")
    dateline = dateline + ": " + now
    print(dateline)
    print(linebreak)

    ## prompt for entry
    var = raw_input("Please enter Today's Log Entry: ")
    print("You Entered: ",  var)
    confirm = raw_input("CONFIRM: y/n? ")
    if re.match( r"[Yy]", confirm):
        print("COMMITING to GITHUB")
        progressline = progressline + " "+var
    else: 
        print("aborting.....")

    entry = linebreak + "\n"+ preamble + " \n" + dateline + "\n" + progressline + "\n" + linebreak + "\n"
    print(entry)

    line_prepender("log.md", entry)
    call(["head", "log.md"])
    call(["git", "commit", "-m", "log entry on "+now])
    call(["git", "push"]) 


if __name__ == '__main__':
    main()

