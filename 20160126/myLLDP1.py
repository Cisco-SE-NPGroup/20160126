f = open('lldp.txt', 'r')

while True:
	line = f.readline()
	if len(line) == 0:
		print "No Text"
		break
	else:
		print line

f.close()
