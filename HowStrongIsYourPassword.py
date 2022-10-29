import time
import threading
import secrets
import string
from pystyle import Colors
import os


number = "0123456789"
breakPoint = True

def timeCount():
    secondPassed = 0
    minutesPassed = 0
    hoursPassed = 0
    while breakPoint == True:
        secondPassed += 1 
        time.sleep(1)
        if secondPassed == 60:
            secondPassed = 0
            minutesPassed += 1
            if minutesPassed == 60:
                minutesPassed = 0
                hoursPassed += 1

    print(Colors.yellow + "Time passed:", hoursPassed, "hours passed,", minutesPassed, "minutes passed,", secondPassed, "seconds passed" + Colors.white)
    input("Press any key to exit")

password = input(Colors.yellow + "Type here your password > " + Colors.white)
lenght = input(Colors.yellow + "Type lenght > " + Colors.white)
i = 0

completeSetting = string.ascii_lowercase
for i in range(len(password)):
    if password.isupper():
        completeSetting = string.ascii_uppercase

    elif password[i].isupper():
        completeSetting = string.ascii_lowercase + string.ascii_uppercase

    if password[i].isdigit():
        completeSetting = completeSetting + number

    if password.isdigit():
        completeSetting = number


threading.Thread(target=timeCount).start()

while True:
    gag = "".join(secrets.choice(completeSetting) for i in range(int(lenght)))
    print(Colors.white + gag)
    if password == gag:
        print(Colors.green + "Found!:", Colors.white + "'" + gag + "'")
        breakPoint = False
        i = i + 1
        break

    else: 
        i = i + 1
        continue




    
