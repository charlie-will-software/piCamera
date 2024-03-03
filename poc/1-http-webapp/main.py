import logging
import sys
from http.server import ThreadingHTTPServer

# Local imports
import logger
from handler import RequestHandler


log = logging.getLogger(__name__)


def main() -> None:
    logger.configure_initial_logger()
    log.info("---Pi Camera webapp---")

    address = ("", 8000)
    try:
        server = ThreadingHTTPServer(address, RequestHandler)
        server.serve_forever()
    finally:
        RequestHandler.camera.stop_recording()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ctrl-C pressed! Exiting...")
        sys.exit(0)
