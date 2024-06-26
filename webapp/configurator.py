from pydantic import BaseModel, AnyUrl, field_validator
from pydantic_settings import BaseSettings
from typing import List
import yaml
import logging

log = logging.getLogger(__name__)


class Resolution(BaseModel):
    """Resolution Model describing width and height in pixels."""

    width: int
    height: int


class Stream(BaseModel):
    """Stream Model describing an individual camera stream."""

    resolution: Resolution


class Camera(BaseModel):
    """Camera Model describing a singular camera instance.

    Describes a camera as a name containing a stream
    object.
    """

    name: str
    stream: Stream


class Server(BaseModel):
    """Describes the Server settings

    Describes a server contains an ip, port, log level and a host_url
    """

    ip: str
    port: int
    log_level: str
    host_url: AnyUrl


class Configuration(BaseSettings):
    """Loading and formatting for YAML configuration files."""

    server: Server
    camera: List[Camera]

    @classmethod
    def import_settings(cls, file_path: str) -> "Configuration":
        if file_path.endswith(".yaml"):
            return cls._from_yaml(file_path)
        else:
            raise ValueError("Incorrect file type. Only .yaml files are supported.")

    @classmethod
    def _from_yaml(cls, file_path: str) -> "Configuration":
        """Allows loading of configuration from yaml

        Args:
            file_path (str): The path to the YAML file

        Returns:
            dict: The loaded configuration instance as a dictionary
        """

        log.debug(f"Yaml file loading from location:\n{file_path}")
        with open(file_path, "r") as file:
            config_dict = yaml.safe_load(file)
        return cls(**config_dict)

    @field_validator("camera", mode="before")
    def validate_camera(cls, values: list) -> list[Camera]:
        """Validate the camera field in the configuration.

        Args:
            values (list): The values being validated

        Returns:
            dict: The validated values
        """

        log.debug(f"Validating Camera with the following values:\n{values}")
        return [Camera(**item) if isinstance(item, dict) else item for item in values]

    @field_validator("server", mode="before")
    def validate_server(cls, values: dict) -> Server:
        """Validate the server field in the configuration

        Args:
            values (list): The values being validated

        Returns:
            dict: The validated values
        """

        log.debug(f"Validating Server with the following list values:\n{values}")
        return Server(**values)
