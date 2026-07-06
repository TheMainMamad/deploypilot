""" DeployPilot Configuration file """

from os import environ
from dataclasses import dataclass

from deploypilot.utils.helpers import env_to_bool


@dataclass
class Database:
    connection_url: str
    driver: str
    max_pool_size: int
    auto_commit: bool
    expire_on_commit: bool


@dataclass
class RedisCache:
    redis_url: str
    redis_port: int
    redis_user: str = None
    redis_password: str = None


@dataclass
class Logging:
    level: str
    type: str
    file: bool
    console: bool
    format: str


@dataclass
class DeployPilotSettings:
    environment: str
    base_url: str
    base_path: str
    allowed_origins: list[str]
    logging: Logging
    database: Database
    cache: RedisCache | None = None



class ConfigurationLoader:
    def load(self) -> DeployPilotSettings:
        return DeployPilotSettings(
            environment=environ['ENVIRONMENT'],
            base_url=environ['BASE_URL'],
            base_path=environ["BASE_PATH"],
            allowed_origins=environ["ALLOWED_ORIGINS"].split(","),
            logging=Logging(environ["LOG_LEVEL"], environ["LOG_TYPE"],
                            env_to_bool(environ["LOG_FILE"]),
                            env_to_bool(environ["LOG_CONSOLE"]),
                            environ["LOG_FORMAT"]),
            database=Database(environ["DB_CONNECTION_URL"], environ['DB_DRIVER'],
                              int(environ["DB_MAX_POOL_SIZE"]),
                              env_to_bool(environ["DB_AUTOCOMMIT"]),
                              env_to_bool(environ["DB_EXPIRE_ON_COMMIT"])),
        )


config = ConfigurationLoader().load()
