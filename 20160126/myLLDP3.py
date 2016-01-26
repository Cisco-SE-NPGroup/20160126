f = open('lldp.txt')
myList = f.read().split("\n")

MyHostname = myList[9].split()[4]
MyIPaddress = myList[9].split()[6]
MyInterface = myList[9].split()[5]

DSSwitchName = myList[10].split()[2]
DSInterface = myList[7].split()[2]

MyGW = MyIPaddress.split(".")
MyGWNum = int(MyGW[3]) - 1
MyGWIPaddress = MyGW[0]+"."+MyGW[1]+"."+MyGW[2]+"."+str(MyGWNum)

myCMDFile = open("myCMD.txt","w")
myCMDFile.write("configure terminal\n")
myCMDFile.write("hostname "+MyHostname+"\n")
myCMDFile.write("interface "+MyInterface+"\n")
myCMDFile.write("ip address "+MyIPaddress+" 255.255.255.0\n")
myCMDFile.write("description "+"## to "+DSSwitchName+" ##\n")
myCMDFile.write("ip route 0.0.0.0 0.0.0.0 "+MyGWIPaddress+"\n")
myCMDFile.close()

#close the file
f.close()

