import socket
import RPi.GPIO as GPIO
from time import sleep
import math

GPIO.setmode(GPIO.BCM)
motorTop = [6,13,19,26]
motorBot = [12, 16, 20, 21]

for v in motorBot:
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, 0)
for v in motorTop:
    GPIO.setup(v, GPIO.OUT)
    GPIO.output(v, 0)
    
pattern2 = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]

pattern1 = [
 [0,0,0,1],
  [0,0,1,1],
  [0,0,1,0],
  [0,1,1,0],
  [0,1,0,0],
  [1,1,0,0],
  [1,0,0,0],
  [1,0,0,1]
]

    
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("10.33.142.80", 2022))
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
    
    quad = "5"
    
    while True:
        msg = clientsocket.recv(1024)
        msg = msg.decode("utf-8")
        if(len(msg) > 0):
            quad = msg[0]
            print(quad)
        
        #move up and to the left
        patternX = pattern1
        patternY = pattern1
        
        if(quad == "1"):
            patternX = pattern1
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
        
        elif(quad == "2"):
            patternX = pattern2
            patternY = pattern1
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
            
        elif(quad == "3"):
            patternX = pattern2
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
        
        elif(quad == "4"):
            patternX = pattern1
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 0)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)            
            
        elif(quad == "5"):
            patternX = pattern1
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
            
        elif(quad == "6"):
            patternX = pattern2
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 0)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
            
        elif(quad == "7"):
            patternX = pattern2
            patternY = pattern1
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
            
        elif(quad == "8"):
            patternX = pattern1
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)    
        
        elif(quad == "9"):
            patternX = pattern2
            patternY = pattern2
            for j in range(8):#full cycle
                for k in range(4): #Set each output
                    if patternX[j][k] == 1:
                        GPIO.output(motorBot[k], 1)
                        GPIO.output(motorTop[k], 1)
                    else:
                        GPIO.output(motorBot[k], 0)
                        GPIO.output(motorTop[k], 0)
                sleep(0.001)
        
Main()
