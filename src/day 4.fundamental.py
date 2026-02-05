

#Task=1

contacts={"asif":5555,"sakhib":9999,"heer":9669}
print(contacts)

contacts["aman"]=9898 # add new contacts
print(contacts)

contacts["heer"]=9809
print(contacts)


#safe access
print(contacts.get("nida","asif ka kati so hai"))

for a,b in contacts.items():
    print(f"bhadwa: {a} / phone {b}")
    
#Task 2
raw_logs=["ID01","ID02","ID03","ID01","ID04","ID02","ID05"]
unique_users=set(raw_logs)

print("ID05" in unique_users) 

duplicates = len(raw_logs)-len(unique_users)
print("total duplicates removed are",duplicates)

# task 3

#creating two sets
friend_a={"python","cooking","hiking","movies"} 
friend_b={"hiking","gaming","photography","python"}

shared_interests =friend_a&friend_b 
all_interest =friend_a|friend_b
unique_to_a =friend_a-friend_b

print(shared_interests)
print(all_interest)
print(unique_to_a)
