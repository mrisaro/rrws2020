#!/usr/bin/python
import time, serial, sys
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os.path
ser = serial.Serial('/dev/ttyACM0', 9600)
var = [b'T',b'H',b'L']

min = 0.25
hs  = 1

dt  = min*60
N   = hs*int(60/min)
A = []
plt.figure(1)

for ii in range(N):
	a = []
	tt   = datetime.datetime.now().time()

	a.append(str(tt))
	for jj in var:
		ser.write(jj)
		val=float(ser.readline())
		print(val)
		a.append(val)
		time.sleep(2)

	plt.subplot(311)
	plt.plot(ii, a[1],'*',color='C0')
	plt.subplot(312)
	plt.plot(ii, a[2],'*',color='C1')
	plt.subplot(313)
	plt.plot(ii, a[3],'*',color='C2')
	plt.show(block=False)
#	plt.plot(ii, a[1], '*', color='C0') # pyplot will add this data
#	plt.show(block=False) # update plot
	plt.pause(1) # pause

	A.append(a)
	time.sleep(dt)

A = np.reshape(A,(ii+1,4))

file_name = 'data_THL_'+datetime.datetime.now().strftime("%b-%d-%Y")
file_test = file_name + '.csv'
ii = 1
while os.path.isfile(file_test):
	file_name = file_name + '_' + str(ii)
	file_test = file_name + '.csv'
	ii=ii+1

file_name = file_test

np.savetxt(file_name, A, header="time,T,H,L", fmt="%s",
					delimiter=',', comments='')
