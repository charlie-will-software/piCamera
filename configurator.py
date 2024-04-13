from pydantic import BaseModel, AnyUrl, field_validator, root_validator
from pydantic_settings import BaseSettings
from typing import List
import yaml

# Local imports
import logging

log = logging.getLogger(__name__)


class Resolution(BaseModel):
    """Resolution Model describing width and height in pixels."""

    width: int
    height: int


class Streaming(BaseModel):
    """Streaming Model describing an individual camera stream."""

    resolution: Resolution


class Camera(BaseModel):
    """Camera Model describing a singular camera instance.

    Describes a camera as a name containing a streaming
    object.
    """

    name: str
    streaming: Streaming


class Server(BaseModel):
    """Describes the Server settings

    Describes a server containt an ip, port, log level and a host_url
    """

    ip: str
    port: int
    log_level: str
    host_url: AnyUrl


class Configuration(BaseSettings):
    """Loading and formatting for YAML configuration files.

    Handles the loading and formatting of YAML configuration files
    """

    server: Server
    camera: List[Camera]

    @classmethod
    def from_yaml(cls, file_path: str):
        """Allows loading of configuration from yaml

        Args:
            file_path (str): The path to the YAML file

        Returns:
            Configuration: The loaded configuration instance
        """

        log.debug(f"Yaml file loading from loation:\n{file_path}")
        with open(file_path, "r") as file:
            config_dict = yaml.safe_load(file)
        return cls(**config_dict)

    @field_validator("camera", mode="before")
    def validate_camera(cls, values: list) -> dict:
        """Validate the camera field in the configuration.

        Args:
            values (list): The values being validated

        Returns:
            dict: The validated values
        """

        log.debug(f"Validating Camera with the following values:\n{values}")
        return [Camera(**item) if isinstance(item, dict) else item for item in values]

    @field_validator("server", mode="before")
    def validate_server(cls, values: list) -> dict:
        """Validate the server field in the configuration

        Args:
            values (list): The values being calidared

        Returns:
            dict: The validated values
        """

        log.debug(f"Validating Server with the following list values:\n{values}")
        return Server(**values)
