import os
import time

devices = []

os.system("arp -a > temp.txt")

f = open("temp.txt", "r")
for line in f:
	temp = line.partition('at')
	temp2 = temp[2]
	temp = temp2.rpartition('on')
	temp2 = temp[0]
	print temp
	print temp2
f.close()

os.system("rm temp.txt")
