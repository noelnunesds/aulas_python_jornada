from loguru import logger 
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}<g/> {file}",
    level="CRITICAL"
)

