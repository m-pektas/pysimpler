import logging

pysimpler_logger = logging.getLogger("PYSIMPLER")
pysimpler_logger.setLevel(logging.DEBUG)
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(format)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
pysimpler_logger.addHandler(ch)
