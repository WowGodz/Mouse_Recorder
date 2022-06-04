import subprocess
password = open('password.txt', 'r')
password = password.readline()
pw = input('password :')
q = False
a = 0
run = False
if pw == password and a == 0:
    print('access granted')
    a = 1
    q = True
else:
    print('access denied')
    run = False

if q:
    access = input('*Do you wish to replace password* \n'"    (Y/N) to continue:")
    access = access.lower()
    if access == ("y" or "yes"):
        b = input('enter recent password: ')
        if b == password:
            s = open('password.txt', 'w+')
            s.writelines(input('create new password: '))
    elif access == "n" or "no":
        print('Please wait ....')
        run = True

if run:
    subprocess.call("menu.py", shell=True)


