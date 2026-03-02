#!./venv/bin/python

import os

class Settings:
    APP_NAME: str = "Cloud Diagnostic Service by Ch1"
    VERSION: str = "0.0.1"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")
    GIT_COMMIT = str = os.getenv("GIT_COMMIT", "unknown")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO") # type: ignore

settings = Settings()

#print("App name: ", settings.APP_NAME)
print(settings.LOG_LEVEL)