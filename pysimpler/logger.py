import logging

logger = logging.getLogger("PYSIMPLER")
logger.setLevel(logging.DEBUG)
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(format)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
