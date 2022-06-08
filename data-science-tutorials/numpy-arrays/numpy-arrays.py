#Getting started
#Numpy arrays are great alternatives to Python Lists. Some of the key advantages of 
# Numpy arrays are that they are fast, easy to work with, and give users the opportunity 
# to perform calculations across entire arrays.
#In the following example, you will first create two Python lists. Then, you will 
# import the numpy package and create numpy arrays out of the newly created lists.


height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
print(type(np_weight))

#Element wise calculations
#Now we can perform element-wise calculations on height and weight. For example, you 
# could take all 6 of the height and weight observations above, and calculate the BMI 
# for each observation with a single equation. These operations are very fast and 
# computationally efficient. They are particularly helpful when you have 1000s of 
# observations in your data.

# Calculate bmi
bmi = np_height / np_weight ** 2
print (bmi)

#Subsetting
#Another great feature of Numpy arrays is the ability to subset. For instance, if 
# you wanted to know which observations in our BMI array are above 23, we could 
# quickly subset it to find out.

#boolean
bmiGreaterThan23Bool = bmi > 0.000221
print(bmiGreaterThan23Bool)

#print only those > 0.000221
bmiGreaterThan23PrintSelected = bmi[bmi > 0.000221]
print(bmiGreaterThan23PrintSelected)

