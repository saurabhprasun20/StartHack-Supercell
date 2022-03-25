from flask import Flask, render_template
from flask_socketio import SocketIO, emit
# from smodel import genResults, getBertAnswer
# from test import add

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print("Connected")

@socketio.on('message')
def test_connect(data):
    print("Welcome, messages received")
    print(data)
    return_data=""
    if data.startswith("Hello"):
        return_data = "Hello!! How are you?"
    elif data == "I am always angry":
        return_data = "Maybe you should meditate regularly"
    elif data == "I am so happy for your promotion.":
        return_data = "Thanks mate. Means a lot to me."
    else:
        return_data = "I am only a chatbot!! I am quite dumb and can't understand everything"
    # print("About to emit the message")
    emit('message', return_data)

@socketio.on('disconnect')
def test_disconnect(): 
    print('Client disconnected')

if __name__ == '__main__':
    app.run(port=8000)
