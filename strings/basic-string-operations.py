import string


astring = "Hello World!"
astring2 = 'Hello World!'

print("single quotes are ' '")
print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[-1]) #start by the end
print(astring[3:7:2]) #this prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step]
print(astring[3:7])
print(astring[3:7:1])
print(astring[::-1]) #reverse string
print(astring.upper()) #uppercase
print(astring.lower()) #lowercase

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords[0])
print(afewwords[1])