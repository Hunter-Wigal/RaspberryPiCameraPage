from flask import Flask, render_template, Response, url_for, request
import picamera2
import time
import cv2
import os

os.environ.setdefault("FLASK_DEBUG", "1")
 
app = Flask(__name__)

# Set up camera
picam2 = Picamera2()
config = picam2.create_video_configuration(...)
picam2.configure(config)
picam2.start_preview()

 
@app.route('/')
def hello_world():
    if request.method == "POST":
        height = request.form['height']
        
    if request.method == "GET":
        stream = io.BytesIO()
        picam2.capture(stream, 'jpeg', use_video_port=True)
        stream.seek(0)
        img = Image.open(stream)
        return render_template("index.html", img=img)
        
    return render_template("index.html")



@app.route('/test', methods=["POST",  "GET"])
def test_post():
    return "Hello"
 

if __name__ == '__main__':
    print("Running application")
    app.run(debug=True, host= '192.168.0.251', port=7000)