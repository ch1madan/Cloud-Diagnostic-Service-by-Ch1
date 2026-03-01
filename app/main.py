#!./venv/bin/python

import os
import socket
import platform
from fastapi import FastAPI

app = FastAPI(
    title="Cloud Diagnostic Service by Ch1",
    version="0.0.1"
)

APP_VERSION = "0.0.1"
GIT_COMMIT = os.getenv("GIT_COMMIT", "unknown") #for CI/CD GitHub Actions или GitLab CI
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")   #В настройках GitHub Actions, GitLab CI или внутри Docker-контейнера принудительно устанавливается ENVIRONMENT=production. Программа видит это значение, отключает опасные отладочные функции и подключается к боевым серверам.

"""
Классический Health Check эндпоинт (обычно на фреймворке FastAPI или Flask).
Его задача: сказать системе мониторинга, что приложение «живо», и показать, 
какая именно версия кода сейчас запущена.
"""
@app.get("/health")                         # декоратор, который создает маршрут (путь) /health
def health():                               # определяем функцию health
    return {                                # в FASTapi возвращаемый словарь Python автоматически превращается в JSON.
        "status":"OK! Diagnostic APP is running!",
        "version":APP_VERSION,
        "git_commit":GIT_COMMIT
    }

@app.get("/info")
def info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "platform": platform.system(),
        "Environment": ENVIRONMENT
    }