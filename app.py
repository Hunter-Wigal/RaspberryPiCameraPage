from flask import Flask, render_template, Response, url_for, request
from picamera2 import Picamera2
import time
import cv2
import os

os.environ.setdefault("FLASK_DEBUG", "1")
 
app = Flask(__name__)


def generate_frames():
    with Picamera2() as camera:
        camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        camera.start()
        while True:
            frame = camera.capture_array()
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

 
@app.route('/')
def hello_world():
    if request.method == "POST":
        height = request.form['height']
        
        
    return render_template("index.html")



@app.route('/test', methods=["POST",  "GET"])
def test_post():
    return "Hello"
 

#if __name__ == '__main__':
print("Running application")
    

app.run(debug=True, host= '192.168.0.251', port=7000)
