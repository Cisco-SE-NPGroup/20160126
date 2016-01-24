f = open('lldp.txt', 'r')

line = f.read().split('\n')
print line[7]
print line[9]
print line[10]	

f.close()
