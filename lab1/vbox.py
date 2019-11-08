#!/usr/bin/python3
import datetime
import subprocess
import sys

app2run = "/usr/bin/virtualbox /home/spar/VirtualBox\ VMs/Ubuntu\ 16\ Desk\ sys400\ Ubuntu\ 16\ Desk\ sys400.vbox"
vboxDict = {(1,8):"systems", (3,8):"systems", (0,8):"net", (2,8):"net", (0,13):"logs", (2,13):"logs", (1,13):"other", (3,13):"other", (4,8):"other", (4,13):"other"}

def dh():
    #get the date and hour at runtime
    dh = datetime.datetime
    time = dh.today()
    day = time.weekday()
    hour = time.hour
    return [day , hour]

def vbox(mylist):
    for key in vboxDict:
        if key == mylist:
            return key

def main():
    alist = dh()
    vm = vbox(alist)
    print(vm)
    files = subprocess.Popen(app2run, shell=True)


if __name__ == "__main__":
    main()



