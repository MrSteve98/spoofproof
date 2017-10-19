import os
import time
while True:
	devices = []
	
	os.system("arp -a > temp.txt")
	
	f = open("temp.txt", "r")
	for line in f:
		if line.startswith("gateway"):
			temp = line.rpartition("at ")
			temp2 = temp[2]
			temp = temp2.partition(" [")
			gateway = temp[0]
			devices.append(gateway)
#			print "Gateway: " + gateway
			
		else:
			temp = line.partition('at ')
			temp2 = temp[2]
			temp = temp2.rpartition('on ')
			interface = temp[2]
			temp2 = temp[0].partition(' [')
			temp2 = temp2[0]
			for i in devices:
				if i == temp2:
					print "Possible Man-in-the-Middle attack run by %s on %s!" % (temp2, interface)
			devices.append(temp2)
#f.close()
#os.system("rm temp.txt")
