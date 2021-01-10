import sys
import subprocess

result = subprocess.run(["ping", "8.8.8.8"], capture_output=True, text=True)

t = result.stdout.split(" ")


def parseLine(inputLine):

    if inputLine == "Request timed out.":
        return "Error"
    else:
        inputLine = inputLine.split("=")
        inputLine = inputLine[2]
        inputLine = inputLine.split("ms")
        inputLine = inputLine[0]
        return int(inputLine)


def pingServer(serverAddres):
    Max = 0
    sumOfPings = 0
    result = subprocess.run(["ping", serverAddres], capture_output=True, text=True)
    timeoutsAndErrors = 0
    t = result.stdout.split("\n")
    attentionMark = ""
    for i in range(4):
        if parseLine(t[2 + i]) == "Error":
            timeoutsAndErrors = timeoutsAndErrors + 1
        else:
            ping = parseLine(t[2 + i])
            sumOfPings = sumOfPings + ping
            if ping > Max:
                Max = ping

    Average = sumOfPings / 4
    if timeoutsAndErrors > 0:
        attentionMark = "<---------"
    return [Average, Max, timeoutsAndErrors, attentionMark]


listOfServers = [
    ["Google Wifi Router", "192.168.86.1", 10],
    ["Main switch", "192.168.86.63", 30],
    ["Cable modem", "192.168.100.1", 20],
    ["SBB DNS", "89.216.1.2", 60],
    ["Test server", "200.200.200.200", 10],
    ["Google DNS", "8.8.8.8", 100],
]
for i in range(len(listOfServers)):
    info = pingServer(listOfServers[i][1])

    if info[1] > listOfServers[i][2]:
        info[3] = "<--------- (Ping too high)"

    print(
        f"Name: {listOfServers[i][0]:20}  IP: {listOfServers[i][1]:16}  Average: {info[0]:5.1f}   Max: {info[1]:5}  Errors:  {info[2]:5}  {info[3]:15}"
    )
