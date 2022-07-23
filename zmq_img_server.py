import zmq
import cv2
import numpy
import base64
import time
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
print("Listening to images")
cam=cv2.VideoCapture("rtsp://192.168.1.7:8080/h264_ulaw.sdp")

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(320,240),cv2.INTER_AREA)
    encoded,buffer=cv2.imencode('.jpg',frame)
    data=base64.b64encode(buffer)
    #print(data)
    socket.send(data)
    print("streameing frame")
    #time.sleep(1)
video_capture.release()
cv2.destroyAllWindows()

