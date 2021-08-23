# from youtube hash tech coders

import datetime

name = input("Enter your name :")
age = input("Enter your age :")

now= datetime.datetime.now()
diff = 100 - int(age)
print("Hi " + name + " you will complete 100 in", (now.year+diff))
