from enum import Enum


class MLFrameworks(Enum):
    KERAS = "keras"
    TENSORFLOW = "tensorflow"
    PYTORCH = "pytorch"
    DEFAULT = "default"


class TIME_UNITS(Enum):
    NANOSECONDS = "ns"
    MILLISECONDS = "ms"
    SECONDS = "sec"
    MINUTES = "min"
    HOURS = "hour"
