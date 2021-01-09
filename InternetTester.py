import sys
import subprocess
print("Hello world")
result = subprocess.run(
    ["ping", "8.8.8.8"], capture_output=True, text=True)

print("stoudt:", result.stdout)
print("stderr", result.stderr)
t = result.stdout.split(' ')
#10, 15, 20, 25
ping1 = t[10]
ping2 = t[15]
ping3 = t[20]
ping4 = t[25]

def parseLine(inputLine): 
    inputLine = inputLine.split('=')
    inputLine = inputLine[1]
    inputLine = inputLine.split('ms')
    inputLine = inputLine[0]
    return int(inputLine)

def pingServer (serverAddres):

    result = subprocess.run(
    ["ping", serverAddres], capture_output=True, text=True)

    t = result.stdout.split(' ')

    ping1 = t[10]
    ping2 = t[15]
    ping3 = t[20]
    ping4 = t[25]

    ping1 = parseLine(ping1)
    ping2 = parseLine(ping2)
    ping3 = parseLine(ping3)
    ping4 = parseLine(ping4)



    #print(ping1, ping2, ping3, ping4)

    #Average
    #print("Average:", (ping1+ping2+ping3+ping4)/4)
    Average = (ping1+ping2+ping3+ping4)/4

    #Maximum
    #print("Max", max(ping1,ping2,ping3,ping4))
    Max = max(ping1,ping2,ping3,ping4)
    return[Average, Max]



listOfServers = [["Google DNS", "8.8.8.8"], ["Main switch","192.168.86.63" ], ["Google Wifi Router", "192.168.86.1"], ["Cable modem", "192.168.100.1"], ["SBB DNS", "89.216.1.2"]]
for i in range(len(listOfServers)):
    info = pingServer(listOfServers[i][1])
    print(str(listOfServers[i][0]) + "   IP:" + str(listOfServers[i][1]) + "   Average:" + str(info[0]) + "   Max:" + str(info[1]))
