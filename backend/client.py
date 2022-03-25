from socketIO_client import SocketIO, LoggingNamespace
import socketio
from process_chat import user_input
sio = socketio.Client()

def receivedMessage(args):
    print('Bot: ', args)

socketIO = SocketIO('localhost', 8000, LoggingNamespace)
socketIO.on('message', receivedMessage)

while True:
    msg1 = input("You:")
    print("User: "+msg1)
    socketIO.emit('message',msg1)
    socketIO.wait(seconds=5)   
    user_input(msg1)
