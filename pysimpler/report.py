"""Report script"""


import os
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from .enums import TIME_UNITS


class Reporter:
    """Reporter class"""

    report_cache = defaultdict()
    root = "pysimpler_report"
    time_unit = TIME_UNITS.SECONDS

    @classmethod
    def add(cls, key, val, time_unit=TIME_UNITS.SECONDS):
        """Add a new data to the report cache"""
        if cls.report_cache.get(key) is None:
            cls.report_cache[key] = [val]
        else:
            cls.report_cache[key].append(val)

    @classmethod
    def report(cls):
        """Generate report"""
        if os.getenv("PYSIMPLER") != "1":
            return

        os.makedirs(cls.root, exist_ok=True)

        cls.frequency_report()
        cls.average_time_report()

    @classmethod
    def frequency_report(cls):
        """Generate frequency report"""
        xvals = []
        yvals = []
        for key, val in cls.report_cache.items():
            xvals.append(key)
            yvals.append(len(val))

        d = {"functions": xvals, "frequency": yvals}
        df = pd.DataFrame.from_dict(d)

        fig = px.bar(df, x="functions", y="frequency", title="Frequency")
        fig.write_html(f"{cls.root}/function_frequency.html")

    @classmethod
    def average_time_report(cls):
        """Generate time report"""
        xvals = []
        yvals = []
        for key, val in cls.report_cache.items():
            xvals.append(key)
            yvals.append(np.mean(val))

        d = {"functions": xvals, "average_time": yvals}
        df = pd.DataFrame.from_dict(d)
        fig = px.bar(
            df,
            x="functions",
            y="average_time",
            title=f"Average Time ({cls.time_unit.value})",
        )
        fig.write_html(f"{cls.root}/function_average_time.html")

    @classmethod
    def set_time_unit(cls, time_unit):
        """Set time unit"""
        cls.time_unit = time_unit
        return cls.time_unit

    @classmethod
    def set_digits(cls, digits):
        """Set digits"""
        cls.digits = digits
        return cls.digits
