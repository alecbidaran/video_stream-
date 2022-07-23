import zmq
import cv2
import numpy as np
import base64
context = zmq.Context()
print("Connecting to hello world server…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE,np.unicode(''))
while True:
    message=socket.recv_string()
    #topic,image=message.split()
    data=np.fromstring(base64.b64decode(message),dtype=np.uint8)
    frame=cv2.imdecode(data,1)
    cv2.imshow("image",frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()
