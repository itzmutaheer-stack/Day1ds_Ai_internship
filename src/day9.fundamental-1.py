lst=[10,20,30]
print(lst)

import pandas as pd

s1=pd.Series([10,20,30,40])
print(s1)

s2=pd.Series([10,20,30,40], index=("a","b","c","d"))
print(s2)
s1.shape

#topic 2
marks = pd.Series([90,85,70], index=("math","science","social"))

print(marks["math"])
print(marks[["math","social"]])

marks["match"]=45

print(marks)

#topic 3
score=pd.Series([20,30,40,50,60,70,80,90])
passed=score[score<60]
print(passed)

first=score[(score>40) & (score<80)]
print(first)

scolar=score[(score>40)|(score<80)]
print(scolar)

# topic 4
import pandas as pd
import numpy as np
num=pd.Series([0,None,30,np.nan,50,60,70,80,90])
print(num.isnull())
print(num.fillna(9999))

#topic 5 
name=pd.Series(["asif","AMAN","heer","wolfy"])
print(name.str.contains("a"))

# lowering a name
low=name.str.lower()
print(low)
print(low.str.contains("a"))

# Task 1
import pandas as pd

# Create the Series with custom labels
products = pd.Series([700, 150, 300,],index=['Laptop', 'Mouse', 'Keyboard'])

# Access the price of 'Laptop' using label-based indexing
laptop_price = products['Laptop']

# Slice the first two products using positional indexing
first_two_products = products.iloc[:2]

# Output results
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst two products (positional slicing):")
print(first_two_products)

# Task 2
import numpy as np
import pandas as pd
grades=pd.Series([85,None,92,45,None,78,55])
print(grades)

null_values=grades.isnull()
print("viewing null values",null_values)

filled_series=grades.fillna(0)
print("viewing missing values",filled_series)

filtered_result=grades[grades<60]
print("viewing fter filtering values",filtered_result) 

# Task 3
import pandas as pd
usernames=pd.Series(['Alice',' bob ',' Charlie_Data ','daisy'])
remove=usernames.str.strip()
print(remove)

low=usernames,str.lower()
contains=low.str.contains('a')
print("Cleaned Series",remove)
print("The boolean result of the 'a' search.",contains)
