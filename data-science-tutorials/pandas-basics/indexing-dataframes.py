#Indexing DataFrames
#There are several ways to index a Pandas DataFrame. One of the easiest ways to 
# do this is by using square bracket notation.
#In the example below, you can use square brackets to select one column of the 
# cars DataFrame. You can either use a single bracket or a double bracket. The 
# single bracket will output a Pandas Series, while a double bracket will output 
# a Pandas DataFrame.

# Import pandas and cars.csv
import pandas as pd
cars = pd.read_csv('C:\\cars.csv', index_col = 0)

print(cars)

# Print out country column as Pandas Series
print(cars['cars_per_cap'])

# Print out country column as Pandas DataFrame
print(cars[['cars_per_cap']])

# Print out DataFrame with country and drives_right columns
print(cars[['cars_per_cap', 'country']])

# Print out first 4 observations
print(cars[0:4])

# Print out fifth and sixth observation
print(cars[4:6])

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']])