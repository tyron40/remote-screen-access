from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

user_socket = None
target_socket = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/target')
def target():
    return render_template('target.html')

@socketio.on('connect')
def handle_connect():
    global user_socket, target_socket
    if request.args.get('type') == 'user':
        user_socket = request.sid
        emit('status', {'message': 'User connected'}, to=target_socket)
    elif request.args.get('type') == 'target':
        target_socket = request.sid
        emit('status', {'message': 'Target connected'}, to=user_socket)

@socketio.on('disconnect')
def handle_disconnect():
    global user_socket, target_socket
    if request.sid == user_socket:
        user_socket = None
    elif request.sid == target_socket:
        target_socket = None

@socketio.on('request_permission')
def handle_request_permission(data):
    emit('permission_request', data, to=target_socket)

@socketio.on('permission_granted')
def handle_permission_granted(data):
    emit('start_monitoring', data, to=user_socket)

@socketio.on('start_screen_share')
def handle_start_screen_share(data):
    emit('start_screen_share', data, to=target_socket)

@socketio.on('stop_screen_share')
def handle_stop_screen_share(data):
    emit('stop_screen_share', data, to=target_socket)

@socketio.on('start_audio_share')
def handle_start_audio_share(data):
    emit('start_audio_share', data, to=target_socket)

@socketio.on('stop_audio_share')
def handle_stop_audio_share(data):
    emit('stop_audio_share', data, to=target_socket)

@socketio.on('take_picture')
def handle_take_picture(data):
    emit('take_picture', data, to=target_socket)

@socketio.on('start_video')
def handle_start_video(data):
    emit('start_video', data, to=target_socket)

@socketio.on('send_screen')
def handle_send_screen(data):
    emit('receive_screen', data, to=user_socket)

@socketio.on('send_audio')
def handle_send_audio(data):
    emit('receive_audio', data, to=user_socket)

@socketio.on('send_picture')
def handle_send_picture(data):
    emit('receive_picture', data, to=user_socket)

@socketio.on('send_video')
def handle_send_video(data):
    emit('receive_video', data, to=user_socket)

@socketio.on('play_sound')
def handle_play_sound(data):
    emit('play_sound', data, to=target_socket)

@socketio.on('receive_sound')
def handle_receive_sound(data):
    emit('receive_sound', data, to=user_socket)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
