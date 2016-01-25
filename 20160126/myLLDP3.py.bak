f=open('lldp.txt')
i=0
myList = f.read().split("\n")
f.close()

myHostname = "hostname  "+myList[9].split(" ")[4]
myIPAddress= myList[9].split(" ")[6]
myIPAddressCMD= "ip address "+myList[9].split(" ")[6]+" 255.255.255.0"
myInterface = "interface "+ myList[9].split(" ")[5]
dsHostname = myList[10].split(":")[1]
dsInterface = myList[7].split(":")[1]
myDescription = '''description "## to %s %s ##"''' %(dsHostname,dsInterface)

myGW=myIPAddress.split(".")
myGWNum=int(myGW[3]) - 1
myGWIPAddress=myGW[0]+"."+myGW[1]+"."+myGW[2]+"."+str(myGWNum)
myRouting = "ip route 0.0.0.0 0.0.0.0 "+myGWIPAddress

## Start CMD File Generation
myCMDFile=open("myCMD.txt","w")
myCMDFile.write("configure terminal\n")
myCMDFile.write(myHostname+"\n")
myCMDFile.write(myInterface+"\n"+myIPAddressCMD+"\n")
myCMDFile.write(myInterface+"\n"+myDescription+"\n")
myCMDFile.write(myRouting+"\n")
myCMDFile.close()


