import os, sys
import subprocess

run = False
if not run:
    run2 = True
run2 = True

# run2 deletes previous files
while run2:
    open("app", "w+")
    os.remove("app.txt")
    open("app.txt", "w+")
    run = True
    run2 = False
while run:
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            # only print lines that are not empty
            # decode() is necessary to get rid of the binary string (b')
            # rstrip() to remove `\r\n`
            file1 = open("app.txt", "a+")
            file1.writelines(str(line.decode().rstrip()) + "\n")
            print(file1.read)
            run = False
