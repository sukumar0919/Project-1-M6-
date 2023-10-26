import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
class Solution_4:
        def __init__(self, df):
            self.df = df
        def task1(self):
            tally = self.df['Make'].value_counts()
            tally.plot(kind='bar', title='Electric Vehicles Sold in Washington State', yticks=[0, 5000, 10000, 15000, 70000])
            category = self.df.Make.value_counts()  
            category_df = category.reset_index()
            category_df.columns = ['categories', 'frequency']
            plt.figure(figsize=(8,6))
            plt.xlabel('Make')
            plt.ylabel('Counts')
            seaborn_plot = sns.barplot(x = 'categories', y = 'frequency', data = category_df)
            for item in seaborn_plot.get_xticklabels():
                item.set_rotation(90)
            return tally
        
        def task2(self):
            tally_model_year = self.df['Model Year'].value_counts()
            tally_model_year
            tally_model_year.plot(kind='bar',title='EVs Sold in each Model Year', yticks=[0, 5000, 10000, 15000, 25000, 40000])
            category = self.df['Model Year'].value_counts()  
            category_df = category.reset_index()
            category_df.columns = ['car sales', 'model year']
            plt.figure(figsize=(8,6))
            plt.xlabel('Model year')
            plt.ylabel('Car Sales')
            seaborn_plot = sns.lineplot(x = 'car sales', y = 'model year', data = category_df)
            for item in seaborn_plot.get_xticklabels():
                item.set_rotation(100)
                return tally_model_year
            
        def task3(self):
             result_dataframe = self.df.groupby(['Electric Utility']) 
             counts = result_dataframe['Make'].value_counts().groupby(level=0).nlargest(10)
             display(counts)
             top_n = 10
             top_counts = counts.nlargest(top_n, keep='all')
             plt.figure(figsize=(17, 6))
             top_counts.plot(kind='bar', color='skyblue')
             plt.title("Top {} Makes by Electric Utility".format(top_n))
             plt.xlabel("Electric Utility")
             plt.ylabel("count")
             plt.show()
             return counts