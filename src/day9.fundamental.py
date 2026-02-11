#topic1
lst=[10,20,30,40]
print(lst)

import pandas as pd

s1 = pd.Series([10,20,30,40])
print(s1)

s2 = pd.Series([10,20,30,40], index = ('a','b','c','d'))
print(s2)
s1.shape

#topic2

marks=pd.Series([85,90,78],index=('Math','Physics','chemistry'))

print(marks['Math'])
print(marks[['Math','chemistry']])

marks['math']=45
print(marks)

#topic3

score =pd.Series([20,30,40,50,60,70,80,90])
passed = score[score<60]
print(passed)

first=score[(score>40)&(score<80)]
print(first)

scolar=score[(score>40)|(score<80)]
print(scolar)

#topic4

import pandas as pd
import numpy as np
num=pd.Series([0,None,30,np.nan,50,60,70,80,90])
print(num.isnull())
print(num.fillna(9999))

#topic5

name=pd.Series(["asif","AMAN","heer","wolfy"])
print(name.str.contains("a"))

# lowering a name
low=name.str.lower()
print(low)
print(low.str.contains("a"))

#task1

import pandas as pd

product=pd.Series([700,150,300],index=['laptop','mouse','keybord'])
print(product)
print(product[['laptop']])
#slicing
print(product[0:2])

#task2
import pandas as pd

num=pd.Series([85,None,92,45,None,78,55])
print(num.isnull())
print(num.fillna(0))

greater_than_60=num[num>60]
print(greater_than_60)

#task3

#Goal: Process text data efficiently using the .str accessor.

#Scenario: A list of usernames was collected with inconsistent casing and extra spaces

# Importing pandas
import pandas as pd

#Create a Series named usernames
usernames=pd.Series( [' Alice', 'bOB', 'Charlie_Data ', 'daisy'])

# Removing leading/trailing whitespace (.strip())
remove=usernames.str.strip()

# Converting all names to lowercase (.lower()).
low=usernames.str.lower()

# Checking which names contain the letter 'a' (.contains()).
contains=low.str.contains('a')

#displaying Cleaned Series
print("Cleaned Series",remove)

#displaying boolean result
print("The boolean result of the 'a' search.",contains)
s
