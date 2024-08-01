Remote Screen Access
A web-based application for remote screen access and monitoring. This project allows a user to remotely view and interact with another device's screen, audio, and camera in real-time.
Features
- Real-time screen sharing
- Audio streaming
- Capture pictures from the remote device
- Record videos from the remote device
- Play sound on the remote device
Technologies Used
- Python
- Flask
- Flask-SocketIO
- HTML
- CSS
- Bootstrap
- JavaScript
Prerequisites
- Python 3.6 or higher
- Flask
- Flask-SocketIO
Setup
1. Clone the repository:
```sh
git clone https://github.com/tyron40/remote-screen-access.git
cd remote-screen-access
```
2. Create and activate a virtual environment:
```sh 
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```
3. Install the dependencies:
```sh
pip install Flask Flask-SocketIO
```
4. Run the application:
```sh
set FLASK_APP=app.py
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=5000
flask run
```
5. Access the application:
Open a web browser and go to `http://localhost:5000` to view the welcome screen.
Usage
1. Welcome Screen:

- Navigate to the `/user` page to access the User Dashboard.
- Navigate to the `/target` page to set up the Target Device.
2. User Dashboard:

- Request permission from the Target Device to access the screen, audio, and camera.
- Use the control buttons to start/stop screen sharing, start/stop audio sharing, take pictures, record videos, and play sound on the Target Device.
- View the shared screen, audio, picture, and video streams on the User Dashboard.
3. Target Device:

- Grant permission to the User for accessing the screen, audio, and camera.
- The Target Device will share the screen, audio, and camera feed as per the User's requests.
File Structure
```
remote-screen-access/
│
├── templates/
│   ├── index.html
│   ├── user.html
│   └── target.html
│
├── app.py
└── README.md
```
License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
Acknowledgments
- Bootstrap for the CSS framework
- Flask and Flask-SocketIO for the web framework and real-time communication
