import socket
import platform
from fastapi import FastAPI, Request
from app.config import settings
from app.logger import setup_logger, logger

setup_logger()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


@app.get("/health")
def health():
    return {
        "status": "ok",
        "version": settings.VERSION,
        "git_commit": settings.GIT_COMMIT,
        "environment": settings.ENVIRONMENT
    }


@app.get("/info")
def info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "platform": platform.system(),
        "environment": settings.ENVIRONMENT
    }