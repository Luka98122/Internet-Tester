import sys
import subprocess
result = subprocess.run(
    ["ping", "8.8.8.8"], capture_output=True, text=True)

t = result.stdout.split(' ')

def parseLine(inputLine): 
    inputLine = inputLine.split('=')
    inputLine = inputLine[2]
    inputLine = inputLine.split('ms')
    inputLine = inputLine[0]
    return int(inputLine)

def pingServer (serverAddres):
    Max = 0
    sumOfPings = 0
    result = subprocess.run(
    ["ping", serverAddres], capture_output=True, text=True)

    t = result.stdout.split('\n')

    for i in range(4):
        ping = parseLine(t[2+i])
        sumOfPings = sumOfPings + ping
        if ping > Max:
            Max = ping

    #print(ping1, ping2, ping3, ping4)

    #Average
    #print("Average:", (ping1+ping2+ping3+ping4)/4)
    Average = sumOfPings/4

    #Maximum
    #print("Max", max(ping1,ping2,ping3,ping4))
    return[Average, Max]

listOfServers = [["Google DNS", "8.8.8.8"], ["Main switch","192.168.86.63" ], ["Google Wifi Router", "192.168.86.1"], ["Cable modem", "192.168.100.1"], ["SBB DNS", "89.216.1.2"]]
for i in range(len(listOfServers)):
    info = pingServer(listOfServers[i][1])
    print(str(listOfServers[i][0]) + "   IP: " + str(listOfServers[i][1]) + "   Average:" + str(info[0]) + "   Max:" + str(info[1]))