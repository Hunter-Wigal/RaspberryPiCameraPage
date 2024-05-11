from flask import Flask, render_template, Response, url_for, request
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
    camera = cv2.VideoCapture(0) 
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/test', methods=["POST",  "GET"])
def test_post():
    return "Hello"
 

if __name__ == '__main__':
 
    app.run(debug=True, host= '192.168.0.11')