from picamera2 import Picamera
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput
import StreamingOutput

# Should this be configured to be an abstract class
# This could mean you could have mutliple cameras on the same pi
class CameraStreamer():
    def __init__(self, name = "default",size = (640,480), streaming_output_hander = StreamingOutput):
        """
        Inputs:
            name - id for the camera
            size - streaming resolution of the samera
            streaming_output_hander - Streaming output handler passed in or default method
        """
        self.picam = Picamera()
        self.configure(picam.create_video_configuration(main={"size":size}))
        self.output = streaming_output_hander()

    def start_recording(self):
        self.picam.start_recording(JpegEncoder(), FileOutput(self.output))
        

    def stop_recording(self):
        self.picam.stop_recording()