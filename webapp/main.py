from flask import Flask

# Local imports
from camera import Camera

app = Flask(__name__)
cam = Camera()
cam.record()


@app.route("/")
def index():


def gen():
    while True:
        frame = cam.output.frame
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run()

