#!/usr/bin/python3
import datetime, subprocess
​
sys2run = "/usr/bin/virtualbox -x /mnt/1C1A722F1A720654/VBOX/SYS500/UbuntuSystems/UbuntuSystems.vbox"
net2run = "/usr/bin/virtualbox -x /home/djv/virtualbox/network/ubuntu_desktop/Clone of Ubuntu_desktop.vmx"
log2run = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu18/ubuntu18.vmx"
oth2run = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu16/ubuntu16/Ubuntu 64-bit.vmx"
​
# The days, time used to call upon the vm need at that time
vboxDict = {(1,8): sys2run, (3,8): sys2run, (0,8): net2run,
    (2,8):net2run, (0,13):log2run, (2,13):log2run,
    (1,13): oth2run, (3,13):oth2run, (4, 8):oth2run,
    (4,13): oth2run}
​
​
def dh():
    # Return the year, month, day, hour, minute, second, and microsecond
    dh = datetime.datetime
    # Return the current local date.
    time =dh.today()
    # Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    day = time.weekday()
    # Hour in range(24)
    hour = time.hour
    # print("Hour: " + str(hour))
    # print("weekday: " + str(day))
    #Return the day and hour to main
    return (day , hour)
    # print("date and hour fuction\n")
    # print(time)
​
def vbox(mylist):
    # print("mylist: " + str(mylist))
    # Pulls the key from virtualboxDict
    for key in vboxDict:
        # print("key :" + str(key))
        #Comparse the key with the current time
        if key == mylist:
            # print("mylist: " + str(vboxDict[key]))
            # If the key is the same run the value in the virtualboxDict
            return vboxDict[key]
​
    # day = list[0]
    # hour = list[1]
    # vboxDict = {[1,8]:"systems",
    # [3.8]:"systems", [0,8]: "network", [2,8]:"network",
    # [0,13]:"logs", [2,13]:"logs", [1,13]:"other",
    # [3,13]:"other", [4, 8]:"other", [4,13]:"other"}
​
    # print("\n virtualbox start fuction")
    # print(day, hour)
​
def main():
    alist = dh()
    # print(list)
    vm = vbox(alist)
    # print ("vm: " + str(vm))
    files = subprocess.Popen(vm, shell=True)
​
    print(files)
​
​
if __name__ == '__main__':
    main()