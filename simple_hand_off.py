


#thread class

import threading;
import time;
import socket;

exitFlag = 0

class myThread (threading.Thread):
    
    def __init__(self, threadID,  name, counter, socket):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.socket = socket   
         
    def run(self):
        print("Starting " + self.name)
        print("Running Thread")
        print("Exiting " + self.name)
        
        
        
#########################################################



print("Starting socket server")

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)    #blocking, waiting for client connection

#while True:
c, addr = s.accept()   #establish connection with client
print ("Got connection from addr" + str(addr))
c.send("Thank you for connecting".encode())
tThread = myThread(1, "Thread-1", 1, c)
tThread.start()
c.close()      #close connection

print("Closing socket server")
    


                
#Create New Threads
#qthread1 = myThread(1, "Thread-1", 1)
#thread2 = myThread(2, "Thread-2", 1)

#Start New Threads
 
#thread1.start()
#thread2.start()
 
#print ("Exiting Main Thread")       
 