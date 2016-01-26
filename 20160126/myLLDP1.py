#i = 0
#f = open('lldp.txt')
#while True:
#	line = f.readline()
#	if len(line) == 0:
#		break
#	else:
#		print 'Line(', i,'): ',line
#	        i = i + 1
#f.close()

#i = 0
#f = open('lldp.txt')
#while True:
#	line = f.readline()
#	if len(line) == 0:
#		break
#	elif i==7 or i==9 or i==10:
#		print 'Line(', i,'): ',line
#        i = i + 1
#f.close()

i = 0
f = open('lldp.txt')
myList = f.read().split("\n")
print 'Line 7th :', myList[7]
print 'Line 9th :', myList[9]
print 'Line 10th :', myList[10]

f.close()
