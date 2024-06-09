# PiCamera Web Server

The PiCamera Web Server is written in Python and utilises the [flask library](https://flask.palletsprojects.com/en/).

## Installation

Running the web server requires an installation of Python 3 and pip. To install these on a debian based linux distribution, run the following commands.

```bash
apt install -y python3 python3-pip python3-picamera2
```

To the dependencies used are in the `requirements.txt` file and can be installed with pip.

> It is recommended that you use a [virtual environment](#setting-up-a-python-virtual-environment).

```bash
pip install -r requirements.txt
```

### Setting up a python virtual environment

The below commands will install the `venv` package, create a virtual environment, and activate the environment. The `--system-site-packages` flag allows the picamera2 module to be used, despite being installed via apt.

```bash
apt install -y python3-venv
python3 -m venv --system-site-packages .venv
. .venv/bin/activate
```

You can exit the virtual environment with the `deactivate` command.

## Running the server

To run the server, make sure you are in the `webapp/` directoy and run the `main.py` file with python.

```bash
flask --app webapp.main:app run --host 0.0.0.0 --port 8000
```
