"""HTTP request handler."""

import logging
from http.server import BaseHTTPRequestHandler

# Local imports
from camera import Camera


log = logging.getLogger(__name__)


class RequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler class.

    Handles HTTP requests to the server.
    """

    camera = Camera()
    camera.record()

    def do_GET(self) -> None:
        """Handles any HTTP GET requests."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Age", 0)
            self.send_header("Cache-Control", "no-cache, private")
            self.send_header("Pragma", "no-cache")
            self.send_header(
                "Content-Type", "multipart/x-mixed-replace; boundary=FRAME"
            )
            self.end_headers()
            self._handle_stream()

    def _handle_stream(self) -> None:
        """Stream live video recording from the camera to the client."""

        try:
            while True:
                with RequestHandler.camera.output.condition:
                    RequestHandler.camera.output.condition.wait()
                    frame = RequestHandler.camera.output.frame
                self.wfile.write(b"--FRAME\r\n")
                self.send_header("Content-Type", "image/jpeg")
                self.send_header("Content-Length", len(frame))
                self.end_headers()
                self.wfile.write(frame)
                self.wfile.write(b"\r\n")
        except Exception as e:
            log.warning("Removed streaming client %s: %s", self.client_address, str(e))
