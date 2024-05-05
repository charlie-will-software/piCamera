from flask import Flask, Response, render_template
from typing import Generator

# Local imports
from camera import Camera

app = Flask(__name__)
cam = Camera()
cam.record()


@app.route("/")
def index() -> str:
    """Webapp home page. Returns HTML."""

    return render_template("index.html")


def generate_frames() -> Generator[str]:
    """Generates camera frames and embeds them in a string for HTTP response.

    Yields:
        HTTP response with jpeg image.
    """

    while True:
        frame = cam.output.frame
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/video_feed")
def video_feed() -> Response:
    """Streams a live video feed from the camera."""

    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run()
