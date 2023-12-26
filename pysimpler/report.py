

from collections import defaultdict 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.cm import get_cmap
import os

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

        if len( list(cls.report_cache.keys()))<2:
            return
         
        A = []
        B = []
        for key, val in cls.report_cache.items():
            A.append(key)
            B.append(len(val))

        print(B)
        fig = plt.figure(figsize = (10, 5))
        
        # creating the bar plot
        plt.bar(A, B, color=cls.__get_cmap__(B, cmap="viridis"), 
                width = 0.4)
        
        plt.xlabel("Functions")
        plt.ylabel("Frequency")
        plt.xticks(rotation = 45)
        plt.title("Functions vs Frequency")
        plt.savefig(f"{cls.root}/function_frequency.png", bbox_inches='tight')

    @classmethod
    def average_time_report(cls):

        if len( list(cls.report_cache.keys()))<2:
            return
        
        A = []
        B = []
        for key, val in cls.report_cache.items():
            A.append(key)
            B.append(np.mean(val))

  
        fig = plt.figure(figsize = (10, 10))

        
        
        # creating the bar plot
        plt.bar(A, B, color=cls.__get_cmap__(B), width = 0.4)

        
        plt.xlabel("Functions")
        plt.ylabel("Average Time")
        plt.xticks(rotation = 45)
        plt.title("Functions vs Average Time (sec.)")
        plt.savefig(f"{cls.root}/function_average_time.png", bbox_inches='tight')

    @classmethod
    def __get_cmap__(cls, B, cmap="Reds"):
        
        den = max(B) - min(B)
        if den == 0:
            den = 0.0001

        scaled_data = [(datum-min(B))/den for datum in B]
        
        # get colors corresponding to data
        colors = []
        my_cmap = get_cmap(cmap)
        
        for decimal in scaled_data:
            colors.append(my_cmap(decimal))
        return colors

