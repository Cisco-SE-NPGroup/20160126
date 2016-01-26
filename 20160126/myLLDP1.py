f=open('lldp.txt')
i=0
while True:
	line=f.readline()
	if len(line)==0:
		print 'No line from fine'
		break
	else:
		print 'LineNumber',i,line
		i=i+1
f.close()
