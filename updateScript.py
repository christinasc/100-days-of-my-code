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


def get_entry_number(): 
    headFile =""
    count = 0
    with open("log.md") as f:
        headFile = (f.read(200))        

    dayNumber = re.search(r"Day [0-9][0-9]:", headFile)
    if dayNumber:
        dayString = str(dayNumber.group(0))
        dayArray = dayString.split()
        dayNum = dayArray[1].split(':')
        count = int(dayNum[0])
        count = count + 1
        print(" Matches:", dayNum[0], count)    
    else: 
        print(" no match ")

    return count


def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


def main():
    linebreak = "----------------------------"
    preamble = "# 100 Days Of Code - Log "
    dateline = "### Day "
    progressline = "**Today's Progress**: "
    thoughtline = "**Thoughts**: "
    linkline= "**Link to work**: "

#   call(["ls", "-l"])
#   call(["git", "status"])
    print(linebreak)

    now = time.strftime("%c")
    
    entryNumber = get_entry_number()

    dateline = dateline + str(entryNumber) +  ": " + now
    print(dateline)
    print(linebreak)

    ## prompt for entry
    log = raw_input("Please enter Today's Log Entry: ")
    thought = raw_input("Thoughts: ")
    link  = raw_input("Link to Work: ")

    progressline = progressline +  log + "\n"
    thoughtline  = thoughtline + thought + "\n"
    linkline = linkline + link + "\n"

    entry = preamble + "\n\n" + dateline + "\n" + progressline
    entry = entry + thoughtline +  linkline + "\n" + linebreak

    print("You Entered: \n",  entry)
    
    confirm = raw_input("CONFIRM: y/n? ")
    if re.match( r"[Yy]", confirm):
        print("COMMITING to GITHUB THE FOLLOWING")
        line_prepender("log.md", entry) 
        call(["head", "log.md"])
        call(["git", "commit", "-m", "log update on "+now, "log.md"])
        call(["git", "push"])



    else: 
        print("aborting.....")




if __name__ == '__main__':
    main()


