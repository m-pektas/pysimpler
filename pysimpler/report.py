

from collections import defaultdict 
import numpy as np
import matplotlib.pyplot as plt 
import os
import pandas as pd
import seaborn as sns

class reporter:
    
    report_cache = defaultdict()
    root = "pysimpler_report"

    @classmethod
    def add(cls, key, val):

        if cls.report_cache.get(key) == None:
            cls.report_cache[key] = [val]
        else:
            cls.report_cache[key].append(val)

    @classmethod
    def report(cls):

        if os.getenv("PYSIMPLER") != "1":
            return
        
        os.makedirs(cls.root, exist_ok=True)

        cls.frequency_report()
        cls.average_time_report()
        
    @classmethod    
    def frequency_report(cls):
         
        A = []
        B = []
        for key, val in cls.report_cache.items():
            A.append(key)
            B.append(len(val))

        d = {'functions': A, 'frequency': B}
        df = pd.DataFrame.from_dict(d)
        plt.figure()
        ax = sns.barplot(x='functions', y='frequency', data=df)
        ax.bar_label(ax.containers[0])
        plt.xticks(rotation = 45)
        plt.title("Functions vs Frequency")
        plt.savefig(f"{cls.root}/function_frequency.png", bbox_inches='tight')

    @classmethod
    def average_time_report(cls):
        A = []
        B = []
        for key, val in cls.report_cache.items():
            A.append(key)
            B.append(np.mean(val))

        d = {'functions': A, 'average_time': B}
        df = pd.DataFrame.from_dict(d)
        plt.figure()
        ax = sns.barplot(x='functions', y='average_time', data=df)
        ax.bar_label(ax.containers[0], fmt='%f')
        plt.xticks(rotation = 45)
        plt.title("Functions vs Average Time (sec.)")
        plt.savefig(f"{cls.root}/function_average_time.png", bbox_inches='tight')
  

    @classmethod
    def colors_from_values(cls, values, palette_name):
        # normalize the values to range [0, 1]
        normalized = (values - min(values)) / (max(values) - min(values))
        # convert to indices
        indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
        # use the indices to get the colors
        palette = sns.color_palette(palette_name, len(values))
        return np.array(palette).take(indices, axis=0)

