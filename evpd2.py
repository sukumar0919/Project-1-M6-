import pandas
import seaborn
import matplotlib.pyplot as plt
from IPython.display import display

class Solution_1:
        def __init__(self, df):
            self.df = df
        def task2(self):
            
###The chosen dataset comprises electric vehicle data sourced from the State of Washington, accessible through Data.gov. 
            dataframe = pandas.read_csv('../Electric_Vehicle_Population_Data.csv')

# Use Case 1: Vehicle Make Analysis

### Objective: Determine the distribution of electric vehicles by make in the dataset.
### Attributes: VIN (1-10), Make
### Description: In this use case, we aimed to understand the distribution of electric vehicles by their make. The VIN (1-10) column represents the Vehicle Identification Number, while the Make column contains the manufacturer's name. By analyzing this data, we can identify which electric vehicle makes are present in the dataset and gain insights into the diversity of manufacturers.

# Use Case 2: Sales Trends by Model Year

### Objective: Analyze the trends in electric vehicle sales over different model years.
### Attributes: VIN (1-10), Model Year
### Description: In this use case, we focused on understanding the trends in electric vehicle sales by model year. The VIN (1-10) represents the Vehicle Identification Number, and the Model Year column contains information about the year in which the vehicles were manufactured. By visualizing and analyzing this data, we can identify patterns and trends in sales over time, which may reveal important insights into the evolution of electric vehicle adoption.

# Use Case 3: Manufacturer-Utility Associations

### Objective: Determine the associations between electric vehicle makes and the electric utilities they are associated with.
### Attributes: VIN (1-10), Make, Electric Utility
### Description: In this use case, we explored the relationships between electric vehicle makes, the first part of the Vehicle Identification Number (VIN), and the electric utilities they are associated with. The Make column represents the manufacturer's name, and the Electric Utility column contains information about the utility provider. By analyzing this data, we can understand which electric utilities are associated with specific manufacturers and gain insights into the distribution of electric vehicle makes across different utilities in Washington State.

# Attributes
# VIN (1-10)  County	 City	State	Postal Code	Model Year	Make	Model	Electric Vehicle Type	Clean Alternative Fuel Vehicle (CAFV) Eligibility	Electric Range	Base MSRP	Legislative District	DOL Vehicle ID	Vehicle Location	Electric Utility	2020 Census Tract


             # Display the first 10 rows in a tabular format
            display(dataframe.head(10))
        
       
            display(dataframe.dtypes)
           