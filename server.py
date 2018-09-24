from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/from_pi')
def from_pi():
    socketio.emit('refresh', {'data': 'you need to refresh now!'}, broadcast=True)
    return render_template('./response_for_pi.html')

if __name__ == '__main__':
    socketio.run(app)
