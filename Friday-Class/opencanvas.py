#!/usr/bin/python3
import datetime
import subprocess

systems = ("/usr/bin/VBoxManage startvm UbuntuSystems")
networks = "/usr/bin/virtualbox -x /home/djv/virtualbox/network/ubuntu_desktop/Clone of Ubuntu_desktop.vmx"
logs = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu18/ubuntu18.vmx"
strategy = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu16/ubuntu16/Ubuntu 64-bit.vmx"
python = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu16/ubuntu16/Ubuntu 64-bit.vmx"
sec_culture = "/usr/bin/virtualbox -x /home/djv/virtualbox/other/ubuntu16/ubuntu16/Ubuntu 64-bit.vmx"

# The days, time used to call upon the vm need at that time
vboxDict = {(4,13): systems, (3,8): systems, (0,8): networks,
    (2,8):networks, (0,13):logs, (2,13):logs}

URLDict = { systems: "https://secureset.instructure.com/courses/1161", 
    networks: "https://secureset.instructure.com/courses/1152", 
    logs: "https://secureset.instructure.com/courses/1143", 
    strategy: "https://secureset.instructure.com/courses/1149", 
    python: ""}

def dh():
    # Return the year, month, day, hour, minute, second, and microsecond
    dh = datetime.datetime
    # Return the current local date.
    time = dh.today()
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

def vbox(mylist):
    # print("mylist: " + str(mylist))
    # Pulls the key from virtualboxDict
    for key in vboxDict:
        # print("key :" + str(key))
        #Comparse the key with the current time
        if key == mylist:
            # print("mylist: " + str(vboxDict[key]))
            # If the key is the same run the value in the virtualboxDict
            classN = vboxDict.get(key)
            for key in URLDict:
                if key == classN:
                    return URLDict.get(key)

def main():
    alist = dh()
    # print(list)
    vm = vbox(alist)
    url = "google-chrome "+str(vm)
    # print ("vm: " + str(vm))
    files = subprocess.Popen(url, shell=True)
    print(files)

if __name__ == '__main__':
    main()
