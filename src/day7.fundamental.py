# topic 1
# creting a file
file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

#writing a file
file=open("sample.txt","w")
file.write("hello")
file.close()

# writing a append
file=open("sample.txt","a")
file.write("welcome every one")
file.close()

#topic 2
with open("sample.txt","r") as file:
    contnt=file.read()
    print(content)

# topic 3
#create a data.csv files
import csv

with open("muth.csv") as file:
    reader=csv.reader(file) 
    for row in reader: 
        print(row)
        
 # topic 4 

try:
    with open("new.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error, please check the filename")  

# task 1
name=input("enter your name:")
name=input("enteryour daily goal:")

with open("journal.txt","a") as file:
    file.write(f"{name}-{"goal"}\n")

with open("journal.txt","r")as file:
    a=file.read()
    print(a)
    
#task2
import csv

with open("students.csv","r")as file:
    reader=csv.DictReader(file)
    
    print("students who has passed:")
    for row in reader:
        if row ["Status"]=="Pass":
            print(row["Name"])
            
# task 3


filename = input("Enter the filename (e.g., config.txt): ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")   
    
        
            
            
    

        
    