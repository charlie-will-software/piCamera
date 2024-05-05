from flask import Flask, Response
from picamera import PiCamera
import io
import time

app = Flask(__name__)


@app.route("/")
def index():
    return "Video Streaming Server"


def stream():
    with PiCamera() as camera:
        # Set camera resolution as needed
        camera.resolution = (640, 480)
        # Pre-allocate a buffer to speed up capture
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, "jpeg", use_video_port=True):
            # Reset the stream position to the beginning
            stream.seek(0)
            # Read the stream into memory as jpeg
            frame = stream.read()
            # Yield the frame in the response
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")

            # Reset the stream for the next frame
            stream.seek(0)
            stream.truncate()

            # Add a small delay to reduce CPU usage
            time.sleep(0.1)


@app.route("/video_feed")
def video_feed():
    return Response(stream(), mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
