name="shruti"
print(name.title())
#there is no concept of character in python.one chzracter is also a string
c='C'
print(type(c))
print(len(c))
#length starts from 1 always in python not 0
print(name.upper())
print(name.lower())
print(name.title())
#only first letter is captalize
print(name.capitalize())
#means all be in lowercase
print(name.casefold())
#count the s in name
print(name.count('s'))
#-1 will print the last character
print((len(name))-1)
print(name[-1])
#string conversion
age=int("30")
print(type(age))
string="i am immutable and gives error"
# it will error since object doest not support item assignment string[0]='0'
print(string[0:4]) # slicing
print(string[0:4:3])
print(string[::3]) # The character at index 0 is printed first, before any counting. Only then does Python skip 2 characters and print the 3rd one
print(string[::-1]) # reverse the string
print(name[5:])  # All the characters starting from 'i'
print(name[:5])  # All the characters before from 'i'


