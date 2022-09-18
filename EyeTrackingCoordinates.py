import socket
import RPi.GPIO as GPIO
from time import sleep
import math

#Constants
padding = 0.2 #amount on either side where it is full throttle
deadzone = 0.3 #amount in the center where there is no movement
fullThrottleSteps = 10 #how many steps per update at max throttle

#setup gpio
GPIO.setmode(GPIO.BCM)
MotorY = [6, 13, 19, 26]
MotorX = [12,16,20,21]

for v in MotorX:
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, 0)
for v in MotorY:
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, 0)
    

Pattern1 = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

Pattern2 = [
 [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
  [1,0,0,1]
]

#Setup server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.33.142.80", 3434))
s.listen(5)

clientsocket = None
print("Listening")

#Accept clients
while True:
    clientsocket, address = s.accept()
    print("Connection Recieved")
    break

#Recieve data
def Main():
    global x
    global y
    
    while True:
        #Read data
        msg = clientsocket.recv(1024)
        msg = msg.decode("utf-8")
        data = msg.split(";")
        #print(msg)
        x = float(data[0])
        y = float(data[1])
        #print(str(x) + " , " + str(y))
        
        #Determine motor control stuff
        throttleX = Clamp((Clamp(x,0,1)-0.5), -0.5+padding, 0.5 - padding)/(0.5-padding) #-1 to 1
        directionX = throttleX / math.fabs(throttleX)
        throttleX = math.fabs(throttleX)
        if throttleX < deadzone:
            throttleX = 0;
            
        throttleY = Clamp((Clamp(y,0,1)-0.5), -0.5+padding, 0.5 - padding)/(0.5-padding) #-1 to 1
        directionY = throttleY / math.fabs(throttleY)
        throttleY = math.fabs(throttleY)
        if throttleY < deadzone:
            throttleY = 0;
        
        #move motor (more steps for higher numbers)
        PatternX = Pattern1
        PatternY = Pattern2
        if directionX < 0:
            PatternX = Pattern2
        if directionY < 0:
            PatternY = Pattern1
        for i in range (fullThrottleSteps):#more steps for higher throttle
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if j <= fullThrottleSteps * throttleX and PatternX[j][k] == 1:
                        GPIO.output(MotorX[k], 1)
                    else:
                        GPIO.output(MotorX[k], 0)
                    if j <= fullThrottleSteps * throttleY and PatternY[j][k] == 1:
                        GPIO.output(MotorY[k], 1)
                    else:
                        GPIO.output(MotorY[k], 0)
                sleep(0.001)
            if j >= max(fullThrottleSteps * throttleX, fullThrottleSteps * throttleY) :
                break  
            
def Clamp(n, Lower, Upper):
    if n < Lower:
        return Lower
    elif n > Upper:
        return Upper
    else:
        return n
        
Main()
