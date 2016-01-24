f = open('lldp.txt', 'r')

line = f.read().split('\n')
a = line[9].split(" ")[4]
b = line[9].split(" ")[6]
c = line[9].split(" ")[5]
d = line[10].split(':')[1]
e = line[7].split(':')[1]	

print "My hostname:", a
print "IP Address:", b
print "Interface:", c
print "dsHostname:", d
print "dsInterface:", e



f.close()
