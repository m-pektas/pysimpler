"""Report script"""

from collections import defaultdict
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Reporter:
    """Reporter class"""

    report_cache = defaultdict()
    root = "pysimpler_report"

    @classmethod
    def add(cls, key, val):
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
        plt.figure()
        ax = sns.barplot(x="functions", y="frequency", data=df)
        ax.bar_label(ax.containers[0])
        plt.xticks(rotation=45)
        plt.title("Functions vs Frequency")
        plt.savefig(f"{cls.root}/function_frequency.png", bbox_inches="tight")

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
        plt.figure()
        ax = sns.barplot(x="functions", y="average_time", data=df)
        ax.bar_label(ax.containers[0], fmt="%f")
        plt.xticks(rotation=45)
        plt.title("Functions vs Average Time (sec.)")
        plt.savefig(f"{cls.root}/function_average_time.png", bbox_inches="tight")
