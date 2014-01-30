#!/usr/bin/python

import serial
import matplotlib.pyplot as plt
import random
from collections import deque
from sys import argv
import time
import re

ser = serial.Serial(argv[1], 9600);

y = deque()
x = deque()
cont = 0
plt.ion()
plt.ylim([0,1024])
while True:
    message = ser.readline();
    message = re.sub('[^0-9]','',message)
    if (len(message) == 0): continue
    message = float(message)
    #message = (message * 5) / 1023
    if (len(y) >= 50):
        plt.cla()       
        x.popleft()
        y.popleft()
    y.append(message)
    x.append(cont)
    plt.plot(x,y)
    plt.draw()

    cont+=1
