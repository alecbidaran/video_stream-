import cv2 
import base64
import numpy as np 
import zmq
import time
context=zmq.Context()
socket=context.socket(zmq.REQ)
socket.connect("tcp://localhost:8888")
print('Socket bind complete')
print('Socket now listening')
if __name__=="__main__":
    while True: 
        socket.send_string("Image")
        #time.sleep(0.1)
        buffer=socket.recv()
        #topic,img_string=buffer.split(" ")
        #print(topic)
        img=np.frombuffer(base64.b64decode(buffer),np.uint8)
        img=cv2.imdecode(img,1)
        cv2.imshow("ip_cam",img)
        cv2.waitKey(1)
cv2.destroyAllWindows()

