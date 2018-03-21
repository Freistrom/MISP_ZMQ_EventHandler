import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to MISP ZMQ…")
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.0.24:50000")
socket.setsockopt(zmq.SUBSCRIBE, b'misp_json')

while True:
    # Process all parts of the message
    message = socket.recv_multipart()
    print(message)