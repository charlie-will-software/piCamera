import logging
from flask import Flask, Response, render_template
from typing import Generator

# Local imports
import logger
from camera import Camera
from configurator import Configuration

app = Flask(__name__)
camera = None
log = logging.getLogger()


def startup() -> None:
    logger.configure_initial_logger()
    config = Configuration.import_settings("configuration.yaml")
    logger.set_log_level(config.server.log_level)

    log.info("---Picamera webapp---")
    log.info(f"IP address: {config.server.ip}")
    log.info(f"Port: {config.server.port}")
    log.info(f"Log level: {config.server.log_level}")

    resolution = config.camera[0].stream.resolution
    global camera
    camera = Camera(size=(resolution.width, resolution.height))
    camera.record()

    app.run(host=config.server.ip, port=config.server.port)


@app.route("/")
def index() -> str:
    """Webapp home page. Returns HTML."""

    return render_template("index.html")


def generate_frames() -> Generator[str, None, None]:
    """Generates camera frames and embeds them in a string for HTTP response.

    Yields:
        HTTP response with jpeg image.
    """

    while True:
        frame = camera.output.frame
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/video_feed")
def video_feed() -> Response:
    """Streams a live video feed from the camera."""

    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    startup()
