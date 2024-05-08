print("Hello World")
a="????Abhijagatap!!!!! "
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
print(a.replace("Abhi", "jyoti"))
print(a.split("  "))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

print(a.count("a"))
print(len(a))
print(len(a.center(50)))
print(a.count("Abhi"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())