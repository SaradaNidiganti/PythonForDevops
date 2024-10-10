azid="azid:az:iam:12345123:user/sarada"
# splitting the string in build function is : 'split'
print(azid.split("/")[0])
print(azid.split("/")[1])
# list index out of range: error
# print(azid.split("/")[2]) 

# converting uppercase
name = "sarada devops"
print(name.upper())

#converting to lower
name1= "DeVoPs ENGINEER"
print(name1.lower())

# to find lenth of the string
text="Python is important for devops Engineers"
print("the length of the string is : ",len(text))

