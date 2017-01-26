from subprocess import call
from sys import argv

#python time.py testes.txt
#git add testes.txt
#git commit -m "argv-autoupdate"
#git push origin master

addCommand = ["git" , "add" , "*"]
commitCommand = ["git" , "commit" , "-m" , "argv"]
pushCommand = ["git" , "push" , "origin" , "master"]

call(addCommand)
call(commitCommand)
call(pushCommand)
