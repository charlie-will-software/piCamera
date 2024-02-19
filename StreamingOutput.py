import io
from threading import Condition

# Class to handle streaming output
class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        """Init for camera streamer"""
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        """
        Write to streaming output
        Inputs:
            buf - buffer for the sreaming output
        """
        with self.condition:
            self.frame = buf
            self.condition.notify_all()
