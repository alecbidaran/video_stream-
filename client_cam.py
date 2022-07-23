import zmq
import cv2 
import base64
import time 
context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind("tcp://*:8888")

video=cv2.VideoCapture(0)
if __name__=="__main__":
    while True: 
        message=socket.recv_string()
    #time.sleep(1)
        if message=="Image":
          ret,frame=video.read()
    #frame=cv2.resize(frame,(320,240),cv2.INTER_AREA)
          encoded,buffer=cv2.imencode(".jpg",frame)
          buffer=base64.b64encode(buffer)
          socket.send(buffer)
          cv2.waitKey(1)
video.release()
