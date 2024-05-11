from flask import Flask, render_template, Response, url_for, request
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import os

os.environ.setdefault("FLASK_DEBUG", "1")
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    if request.method == "POST":
        height = request.form['height']
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen_frames(): 
    
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    
    # allow the camera to warmup
    time.sleep(0.1)
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # frame = frame.array
    # while True:

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/test', methods=["POST",  "GET"])
def test_post():
    return "Hello"
 

if __name__ == '__main__':
    print("Running application")
    app.run(debug=True, host= '192.168.0.251', port=7000)