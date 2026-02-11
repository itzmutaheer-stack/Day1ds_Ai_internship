import numpy as np
a=5
b=4
r=np.multiply(a,b)
print(r)

arr=np.array([1,2,3])
r=arr*2
print(r)


#Task1
#create 5x3 matrix
import numpy as np
s=np.random.randint(50,100,size=(5,3))
#mean
mean_s=s.mean(axis=0)
#noramalize using broadcast
centered_s=s-mean_s
#out put
print("original s:\",s")
print("mean of the matrix",mean_s)
print("centered of the matrix",centered_s)

#Task 2
#create a 1D array with 0to23
import numpy as np
arr=np.arange(24)
#reshape into [4,3,2]
reshaped=arr.reshape(4,3,2)
#transoprt to 4,2,3
final_array=reshaped.transpose(0,2,1)
print("final shape",final_array.shape)
print(final_array)


