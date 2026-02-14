# task 1

import matplotlib.pyplot as plt

#  Data
study_hours =[1,2,3,4,5,6,7,8]
scores = [50,55,65,70,75,85,90,95]

# Create scatter plot
plt.scatter(study_hours, scores)

# labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Scores")

# show grid for better readability
plt.grid(True)

# display the plot
plt.show()

# task 2

import matplotlib.pyplot as plt

plt.subplot(1,2,1)
categories=["Electronic","Clothing","Home"]
value=[300,450,200]
plt.bar(categories,value)
plt.show()

plt.subplot(1,2,2)
number=[10,20,30]
number2=[10,40,60]

plt.plot(number,number2)
plt.show()


