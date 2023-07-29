""""""
"""
1. How would you confirm that 2 strings have the same identity?
a = "Rajashri"
b = "Rajashri"
print(id(b))
print(id(a))
if a is b:
    print("True")
else:
    print("False")
=========================================================
2. How would you check if each word in a string begins with a capital letter?
s = "Salman Khan"
print(s.istitle())
=========================================================
3. Check if a string contains a specific substring
s = "python is very easy language"
if "python" in s:
    print("True")
else:
    print("False")
=========================================================
4. Find the index of the first occurrence of a substring in a string
s = "python is easy language and python is easy to learn"
print(s.find("easy"))
=========================================================
5. Count the total number of characters in a string
s = "python is easy language and python is easy to learn"
print(len(s))
=========================================================
6. Count the number of a specific character in a string
s = "python is easy language and python is easy to learn"
print(s.count("a"))
=========================================================
7. Capitalize the first character of a string
s = "python is easy language and python is easy to learn"
print(s.capitalize())
o/p: Python is easy language and python is easy to learn
=========================================================
8. What is an f-string and how do you use it?
name = "Rajashri Patil"
age = 25
print(f"My name is {name} and my age is {age}")
o/p:My name is Rajashri Patil and my age is 25
=========================================================
9. Interpolate a variable into a string using format()
name = "Rajashri Patil"
age = 25
print("My name is {} and my age is {}".format(name,age))
==========================================================
10. Check if a string contains only numbers
num = '1284846566'
print(num.isnumeric())
===========================================================
11. Split a string on a specific character
s = "python is very easy to learn"
print(s.split("s"))
o/p:['python i', ' very ea', 'y to learn']
===========================================================
12. Check if a string is composed of all lower case characters
s = "python is very easy to learn"
print(s.islower())
===========================================================
13. Check if the first character in a string is lowercase
s = "python is very easy to learn"
print(s[0].islower())
===========================================================
14. Can an integer be added to a string in Python?
-yess
s = "python is very easy to learn"
s1 = s + ' 123'
print(s1)
===========================================================
15. Reverse the string “hello world”
s = "Hello world"
print(s[::-1])
==========================================================
16. Join a list of strings into a single string, delimited by hyphens (For[a-b-c])
s = ["python", "is", "easy", "language"]
s1 = "-".join(s)
print(s1)
===========================================================
17. Uppercase or lowercase an entire string
s = "Python Is Very Easy To Learn"
print(s.upper())
print(s.lower())
==========================================================
18. Uppercase first and last character of a string(forEx. FisH)
s = "fish"
a = s[0].upper()
b = s[-1].upper()
s1 = a + s[1:3] + b
print(s1)
=========================================================
19. Check if a string is all uppercase
s = "Python is easy language and python is easy to learn"
print(s.isupper())
==========================================================
20. Give an example of string slicing Slicing a string takes up to 3 arguments,
 string[start_index:end_index:step].
s = "Python is easy language and python is easy to learn"
print(s[0:-1:2])
===================================================================
21. Convert an integer to a string
s = 12345
s1 = str(s)
print(s1)
print(type(s1))
===================================================================
22. Check if a string contains only characters of the alphabet
s = "Python"
print(s.isalpha())
===================================================================
23. Replace all instances of a substring in a string
s = "Python is easy language"
print(s.replace("easy", "hard"))
o/p:Python is hard language
===================================================================
24. Check if all characters in a string are alphanumeric
s = "Python123"
print(s.isalnum())
===================================================================
25. Remove whitespace from the left, right or both sides of a string
s = "  Python is easy language  "
print(s.strip())
===================================================================
29. Check if a string begins with or ends with a specific character?
s = "python is easy language"
print(s.startswith("p"))
print(s.endswith("e"))
==================================================================
30. What is the effect of multiplying a string by 3?
s = "Rajashri"
print(s*3)
o/p:RajashriRajashriRajashri
==================================================================
31. Capitalize the first character of each word in a string
s = "saare jahan se accha hindu sita hamara"
print(s.title())
o/p:Saare Jahan Se Accha Hindu Sita Hamara
==================================================================
32. Concatenate two strings
s = "saare jahan se accha"
s1 = "hindu sita hamara"
print(s+s1)
==================================================================
33. Remove vowels from a string (following word:'hello world')
s = 'hello world'
v = "aeiou"
for i in s:
    if i in v:
        continue
    print(i,end='')
==================================================================
34. When would you use rfind()? ex. story = 'The price is right said Bob. The price is right.'
story = 'The price is right said Bob. The price is right.'
print(len(story))
print(story.rfind("is"))
==================================================================
35.Check if a string begins with or ends with a specific character? | following :city = 'New York'
city = 'New York'
print(city.startswith("N"))
print(city.endswith("k"))
==================================================================
"""





