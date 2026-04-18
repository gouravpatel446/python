#strings

#using single quotes
str_1 = 'Hello, World!'
print(str_1)

#using double quotes
str_2 = "Hello, World!"
print(str_2)

# multi-line strings 

str_3 = '''This is a multi-line string.
It can span multiple lines.'''
print(str_3)

# accessing characters in a string
s = "Hello"
print("s[0]:", s[0])
print("s[1]:", s[1])
print("s[2]:", s[2])
print("s[3]:", s[3])
print("s[4]:", s[4])  

# accessing characters in a string using negative indexing
print("s[-1]:", s[-1])  # 'o'
print("s[-2]:", s[-2])  # 'l'
print("s[-3]:", s[-3])  # 'l'
print("s[-4]:", s[-4])  # 'e'
print("s[-5]:", s[-5])  # 'H'   

#string slicing
s = "Hello, World!"
print("s[0:5]:", s[0:5])  # 'Hello' getting chracters from index 1  to 4
print("s[7:12]:", s[7:12])  # 'World' getting characters from index 7 to 11
print("s[:5]:", s[:5])  # 'Hello' getting characters from index 0 to 4

# common string methods
sa= "hello, world!"
print(len(sa))  # length of the string
print(sa.upper())  # convert to uppercase
print(sa.lower())  # convert to lowercase

#string concatenation
str_a = "Hello"
str_b = "world"

str_c = str_a+""+str_b
print(str_c) 

