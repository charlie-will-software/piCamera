from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

# Local imports
from stream import StreamOutput


class Camera(object):
    """Camera class.

    Creates a PiCamera class object and configures it.
    Allows controlled access to the picamera2 object.

    Attributes:
        size: A tuple defining the dimensions of the video recording.
    """

    def __init__(self, size: tuple[int, int] = (640, 480)) -> None:
        """Initialises the camera instance.

        Instantiates a StreamOutput class instance to use as the file output for recording.

        Args:
            size: Defines the dimensions of the video recording.
        """

        self.camera = Picamera2()
        self._configure_camera(size)

        self.output = StreamOutput()

    def _configure_camera(self, size: tuple[int, int]) -> None:
        """Configures the camera video.

        Args:
            size: Defines the dimensions of the video recording.
        """
        print(size)

        self.camera.configure(
            self.camera.create_video_configuration(main={"size": size})
        )

    def record(self) -> None:
        """Starts the camera video recording.

        Uses the software JPEGEncoder.
        """

        self.camera.start_recording(JpegEncoder(), FileOutput(self.output))

    def stop_recording(self) -> None:
        """Stops the camera video recording."""

        self.camera.stop_recording()
