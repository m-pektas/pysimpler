"""Timer module"""
import os
import time
import inspect
from pysimpler.report import Reporter
from .logger import logger
from .enums import TIME_UNITS
from .constants import DIGITS, TIME_UNIT
from .report import Reporter


class Timer:
    """Timer class"""

    def get_func_info(func):
        """This function gives information about the called function."""
        file_path = inspect.getsourcefile(func)  # get filepaht
        file_path = "/".join(file_path.split("/")[-2:])
        name = func.__name__  # get func name
        return file_path, name

    @staticmethod
    def time(digits: str = None, time_unit: TIME_UNITS = None):
        """This function logs duration information of the called function."""

        # set new values if they are not None
        if digits is None:
            digits = DIGITS
        if time_unit is None:
            time_unit = TIME_UNIT

        def decorator(func):
            def wrapper(*args, **kwargs):

                if os.getenv("PYSIMPLER") == "1":
                    function_file_path, function_name = Timer.get_func_info(func)

                    s = time.perf_counter_ns()
                    result = func(*args, **kwargs)
                    e = time.perf_counter_ns()
                    duration_ns = e - s
                    duration = round(Timer.__parse_time(duration_ns, time_unit), digits)
                    logger.info(
                        f"File: {function_file_path} | Function : {function_name} | Duration : {duration} {time_unit.value}"
                    )

                    key = (
                        function_file_path.split("/")[-1].split(".")[0]
                        + "_"
                        + function_name
                    )
                    val = duration

                    if Reporter.time_unit != time_unit:
                        val = round(
                            Timer.__parse_time(duration_ns, Reporter.time_unit), digits
                        )

                    Reporter.add(key, val)
                else:
                    result = func(*args, **kwargs)
                return result

            return wrapper

        return decorator

    def __parse_time(duration, time_unit):
        ms = duration / 1000000
        if time_unit == TIME_UNITS.HOURS:
            return ms / 3600000
        elif time_unit == TIME_UNITS.MINUTES:
            return ms / 60000
        elif time_unit == TIME_UNITS.SECONDS:
            return ms / 1000
        elif time_unit == TIME_UNITS.MILLISECONDS:
            return ms
        elif time_unit == TIME_UNITS.NANOSECONDS:
            return duration
        else:
            raise Exception("Invalid time unit")

    def set_time_unit(time_unit: TIME_UNITS):
        """This function sets the time unit for the duration information."""
        global TIME_UNIT
        TIME_UNIT = time_unit

    def set_digits(digits: int):
        """This function sets the digits for the duration information."""
        global DIGITS
        DIGITS = digits
