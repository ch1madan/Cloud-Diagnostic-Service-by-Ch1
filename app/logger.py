#!./venv/bin/python

import logging
from config import settings

def setup_logger():
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

logger = logging.getLogger("cloud-diagnostic")