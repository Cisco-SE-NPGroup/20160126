f = open('lldp.txt', 'r')

line = f.read().split('\n')
a = line[9].split(" ")[4]
b = line[9].split(" ")[6]
c = line[9].split(" ")[5]
d = line[10].split(':')[1]
e = line[7].split(':')[1]

default = b.split('.')	

myHostname = a
ipAddress = b + " 255.255.255.0"
defaultGateway = default[0] + default[1] + default[2] + '1'
myInterface = c
dsHostname = d
dsInterface = e

g = open('myLLDP3-a.py', 'w')
g.write(myHostname + '\n')
g.write(defaultGateway + '\n')
g.write(myInterface + '\n') 
g.write(dsHostname + '\n')
g.write(dsInterfae + '\n')



g.close()
f.close()
