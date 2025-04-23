# from src.logger import logging

# logging.debug("This is a debug message.")

from src.logger import logging
from src.exception import MyException
import sys

try:
    a = 1 +'2'
except Exception as e:
    logging.info(e)
    raise MyException(e, sys) from e