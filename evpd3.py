import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

class Solution:
        def __init__(self, df):
            self.df = df
 # Display data types and summary statistics in a tabular format
        def task2(self):
            display(self.df.describe())
            self.df['Make'].hist()
            
            