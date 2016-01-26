f=open('lldp.txt')
i=0
myList=f.read().split("\n")

myHostname = myList[9].split()[4]
myIPAddress = myList[9].split()[6]
myInterface = myList[9].split()[5]
dsHostname = myList[10].split(":")[1]
dsInterface = myList[7].split(":")[1]

print "My Hostname : ", myHostname
print "My IP Address : ", myIPAddress
print "My Interface : ", myInterface
print "DS SwitchName : ", dsHostname
print "DS Interface : ", dsInterface

f.close()
