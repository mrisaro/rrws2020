#!/usr/bin/python
import time, serial, sys
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
import datetime
import os.path
ser = serial.Serial('/dev/ttyACM0', 9600)
var = [b'T',b'H',b'L',b'U']

min = 0.5
hs  = 0.5

dt  = min*60
N   = int(hs*int(60/min))
temp  = []
humid = []
light = []
tem   = []
tim   = []

plt.ion() #Tell matplotlib you want interactive mode to plot live data
fig = plt.figure(1,figsize=(10, 6))

def makeFig(): #Create a function that makes our desired plot
#    plt.ylim(80,90)                                 #Set y min and max values
    plt.title('Live streaming sensor data')      	#Plot the title
#    plt.grid(linestlye='--')                  		#Turn the grid on
    plt.ylabel('Temp (C)')                         #Set ylabels
    plt.plot(temp, 'ro-', label='Degrees C')       #plot the temperature
    plt.legend(loc='upper left')                   #plot the legend
    plt2=plt.twinx()                               #Create a second y axis
#    plt.ylim(93450,93525)                         #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(humid, 'b^-', label='Humidity (%)')  #plot humidity data
    plt2.set_ylabel('Humidity')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)         #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                 #plot the legend
##%

def makeFig2():
    ax1 = plt.subplot(311)
    plt.plot(temp,'-o',color='C0')
    plt.setp(ax1.get_xticklabels(), fontsize=6)
    ax1.set_ylabel('Temperatura (C)')
    #ax1.set_ylim(22,26)
    plt.setp(ax1.get_xticklabels(), visible=False)
    # share x only
    ax2 = plt.subplot(312, sharex=ax1)
    plt.plot(humid,'*-',color='C1')
    ax2.set_ylabel('Humedad (%)')
    # make these tick labels invisible
    plt.setp(ax2.get_xticklabels(), visible=False)

    # share x and y
    ax3 = plt.subplot(313, sharex=ax1)
    plt.plot(light,'--',color='C3')
    ax3.set_ylabel('Penumbra (u.a.) ')
    #plt.tight_layout()

for ii in range(N):
    print(str(ii)+' of '+str(N))
    a = []
    tt = datetime.datetime.now().time()
    a.append(str(tt))
    for jj in var:
        ser.write(jj)
        val = float(ser.readline())
        print(val)
        a.append(val)
        time.sleep(2)


    tim.append(a[0])
    temp.append(a[1])
    humid.append(a[2])
    light.append(a[3])
    tem.append(a[4])
    drawnow(makeFig2)
    plt.tight_layout()
    plt.pause(.000001)
    time.sleep(dt)


A = [tim,temp,humid,light,tem]
A = np.transpose(A)
file_name = 'data_THL_'+datetime.datetime.now().strftime("%b-%d-%Y")
file_test = file_name + '.csv'
ii = 1
while os.path.isfile(file_test):
	file_name = file_name + '_' + str(ii)
	file_test = file_name + '.csv'
	ii=ii+1

file_name = 'data/'+file_test

np.savetxt(file_name, A, header="time,T,H,L,t", fmt="%s",
					delimiter=',', comments='')
