"""StreamOutput class."""

from io import BufferedIOBase
from threading import Condition


class StreamOutput(BufferedIOBase):
    """Video stream output class.

    Buffered binary stream output for video.
    """

    def __init__(self) -> None:
        """Initialises the StreamOutput instance."""
        self.frame = None
        self.condition = Condition()

    def write(self, buffer) -> None:
        """Writes frames to a binary stream."""

        with self.condition:
            self.frame = buffer
            self.condition.notify_all()
