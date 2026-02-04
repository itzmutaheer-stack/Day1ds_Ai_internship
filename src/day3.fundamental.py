# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 06:26:32 2026

@author: dell
"""

student_list=["heer",24,8.86]
print(student_list)

car_detail=["bmv",4000000,5]
print(car_detail) # car,price,year

student_list=[10,20,30,40,50,60]
print(student_list) 
#add data in list
student_list=[10,20,30,40,50,60,70]
student_list.append("100")
student_list.pop(2)
print(student_list)

#task1
inventory=["apple","banana","carrots","dates"]
inventory.append('egg')
inventory.remove('banana')
inventory.sort()
print(inventory)

#task2
tempreature=[22,24,25,28,30,29,27,26,24,22]
print(tempreature[0:-1])
tempreature[3:6]
tempreature[-3:]
print("printing the\"afternoon peak(4th,5th,6th iteam)",tempreature[3:6])
print("printing the\"last 3 hour",tempreature[-3])

#task3
screen_res=(1920,1080)
print("current Resolution:1920x1080")
#screen_res[0]=1280
print("Tuples cannot be modify")