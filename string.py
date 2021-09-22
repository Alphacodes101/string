#string
print("Hello")
print('Hello')


#Assign String to a Variable
b= "Hello"
print(b)


#Multiline Strings
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)


#Strings are Arrays
z = "Hello, World!"
print(z[1])


#Looping Through a String
for x in "banana":
  print(x)
  
  
#String Length
d = "Hello, World!"
print(len(d))


#Check String
txt = "The best things in life are free!"
print("free" in txt)



#(slicing in string)
#Slice To the End
n = "Hello, World!"
print(n[2:])


#negative slicing in string
m = "Hello, World!"
print(m[-5:-2])



# modify
#Upper Case
f="hello world!"
print(f.upper())


#lower case string
g="hello world!"
 print(g.lower())   



#white space between srings 
k="hello world!"
print(k.strip())


#replace string 
h = "Hello, World!"
print(h.replace("H", "J"))



#Split String
k= "Hello, World!"
print(k.split(",")) # returns ['Hello', ' World!']





# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

