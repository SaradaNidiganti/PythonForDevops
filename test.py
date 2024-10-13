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

#Slicing: we can get a range of characters in a string by using slice method specify the start index and end index
sliceString = "I love to do programming "
print(sliceString[2:6])
# indexing starts at 0 so l is at 2nd position includedd.. 6 is space or any char if there also (not included) so only in between 2 to 6 like 2,3,4,5
#slice from start 
print(sliceString[:6])
#slice to end
print(sliceString[4:])
# negative indexing, comes from backwards indexing
print(sliceString[-11:-9])

#strip() is used to remove the whitespaces in a string from start & in end
print(sliceString.strip())

# replace() is used to replace a char with another char in a string
print(sliceString.replace(' ','A'))

# split() is used to separate the words in a string to list of items with a special seperator
print(sliceString.split(','))

#string concatination 
a='hi'
b='how are you?'
print(a+b)
print(a+' '+b)

# we can't combine string with numbers like
age = 30
# txt='my age is '+age
# print(txt)

# but we can concate the string and number by using format() or f-string methods
t1=f"my age is: {age}"
print(t1)
# A placeholder can contain variables, operations, functions, and modifiers to format the value.
t2=f'my uncle age is: {age:.2f}'
print(t2)
t3=f'my Dad age is: {2*40}'
print(t3)




