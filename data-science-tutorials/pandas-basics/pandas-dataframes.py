#Pandas DataFrames
#Pandas is a high-level data manipulation tool developed by Wes McKinney. It is 
# built on the Numpy package and its key data structure is called the DataFrame. 
# DataFrames allow you to store and manipulate tabular data in rows of observations 
# and columns of variables.
#There are several ways to create a DataFrame. One way way is to use a dictionary. 
# For example:

dict =  {
            "country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98] 
        }

import pandas as pd

brics = pd.DataFrame(dict)
print(brics)

print("----------")

#As you can see with the new brics DataFrame, Pandas has assigned a key for each 
# country as the numerical values 0 through 4. If you would like to have different 
# index values, say, the two letter country code, you can do that easily as well.

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
# Print out brics with new index values
print(brics)