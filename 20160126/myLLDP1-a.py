f = open('lldp.txt', 'r')
i=0
while True:
	line = f.readline()
	if len(line) == 0:
		print "No Text"
		break
	elif i==7 or i==9 or i==10:
		print line
	i = i+1

f.close()
