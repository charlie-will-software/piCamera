# Streaming webcam as ipcamera

Webcams can easily be accessed via the cv2 library which can be installed by the appropriate opencv install method.

Note that all installations here are only the main modules packages there are extra contributed packages if you are interested see the [open-cv pypi website](https://pypi.org/project/opencv-python/)

## Linux

Make sure opencv is installed first not via pip (you may need to use sudo):

- Fedora: `dnf install opencv`
- Ubuntu: `apt install opencv`

Now use this command to install via pip:

`pip3 install opencv-python`

## Windows

`pip install opencv-python`

# Network Stream Capturing
Captured output for udp example
1. Open vlc
2. In the top bar click the "media" dropdown
3. Then click "Open Network Stream (Ctrl + N)"
4. Enter the stream to capture `udp://@<output-ip>:<output_port>`
    - for the example script: `udp://@127.0.0.1:1234`

## Example using UDP
**Note**:The example below is tested on a Framework 13 Laptop

```python
import subprocess
import cv2

def start_ffmpeg_process(
    width: int, height: int, fps: int, output_ip: str, output_port: int
) -> subprocess.Popen:
    """Function that starts the ffmpeg process with UDP output
    
    Runs subprocess for ffmpeg command that overwrites the existing file
    with the size of the input frame and framerate of the input,
    formatting appropriately for udp streaming to vlc via a given ip
    and output port

    Args:
        width: the width of the input frame as an integer
        height: the height of the inmput frame as an integer
        fps: frames per second of the input
        output_ip: output ip to stream udp output through
        output_port: port to stream udp output through
    Returns:
        subpress.Popen: Process in which ffmpeg is executred
    """
    command = [
        "ffmpeg",
        "-y",  # Overwrite output file if it exists
        "-f",
        "rawvideo",
        "-vcodec",
        "rawvideo",
        "-s",
        f"{width}x{height}",  # Size of the input frame
        "-pix_fmt",
        "bgr24",
        "-r",
        str(fps),  # Frame rate of the input
        "-i",
        "-",  # Read data from standard input
        "-vf",
        "format=yuv420p",  # Format conversion for compatibility with VLC
        "-f",
        "mpegts",  # Output format (MPEG-TS for UDP streaming)
        f"udp://{output_ip}:{output_port}",
    ]

    return subprocess.Popen(command, stdin=subprocess.PIPE)


# Main function to capture webcam feed and stream over UDP
def webcam_to_vlc_stream(
    webcam_id: int = 0,
    output_ip: str = "127.0.0.1",
    output_port: int = 1234,
    width: int = 640,
    height: int = 480,
    fps: int = 30,
):
    """Function to stream webcam output to vlc stream
    
    Using webcam id video capture the output, error is
    raised if the webcam cannot be captured from. If successful
    ffmpeg process is started and the camera frame is written to
    the standard input of the process. If uncommented there is an
    output of the camera from cv2.imshow. When exited appropriately,
    the camera is released. Currently if you fail to exit you receive an error.

    Args:
        webcam_id: id of the camera
        output_ip: output ip of the camera
        Output_port: output port of the camera
        width: resize value for the cameras network stream as pxls (stream output width)
        height: resize value for the cameras network stream as pxls (stream output height)
        fps: fps of the output stream 
    
    Returns:
        None
    """
    cap = cv2.VideoCapture(webcam_id)

    if not cap.isOpened():
        print("Error: Couldn't open webcam.")
        return

    ffmpeg_process = start_ffmpeg_process(width, height, fps, output_ip, output_port)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize frame if necessary
        if frame.shape[1] != width or frame.shape[0] != height:
            frame = cv2.resize(frame, (width, height))

        # Write frame to ffmpeg process
        ffmpeg_process.stdin.write(frame.tobytes())

        # uncomment to see full realtime feed
        #cv2.imshow("Webcam VLC Stream", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    webcam_to_vlc_stream(fps=10
```
