# # Get user input and store as a string
# name : str = input("Enter your name: ")
# # Calculate the length of the name
# name_length = len(name)
# # Print the length of the name
# print(name_length)
# 

# name : str = "Wajid"
# name.count("a")

# print(name.count("a"))

# AGE : int = 24

# print(AGE)


# traffic : str = input("Enter traffic light color (red, yellow, green): ")

# if traffic == "red":
#     print("Stop!")
# elif traffic == "yellow":
#     print("Get Ready!")     
# elif traffic == "green":
#     print("Go!")



# grade : int = int(input("Enter your grade: "))

# if grade >= 90 and grade <= 100:
#     print("A +")
# elif grade >= 80 and grade < 90:
#     print("B")
# elif grade >= 70 and grade < 80:
#     print("C") 
# elif grade >= 60 and grade < 70:
#     print("D")
# else:
#     print("F")



# drive : str = input("Enter your age: ")

# if int(drive) >= 18:
#     if int(drive) >= 80:
#         print("You cannot drive!")
#     else:
#         print("You can drive!")
# else:
#     print("You cannot drive yet!")


# number : int = int(input("Enter a number is odd or even: "))
# if number % 2 == 0:
#     print("Even")
# else:    print("Odd")

# print("Enter the Alphabets to know whos !")
 
# add_num : list = []
# add_num.append(input("Enter first number 1: "))
# add_num.append(input("Enter first number 2: "))
# add_num.append(input("Enter first number 3: "))

# if(add_num[0] == add_num[1] == add_num[2]):
#     print("All numbers are the same!")
# elif(add_num[0] > add_num[1] and add_num[0] > add_num[2]):
#     print("First number is the greatest!")
# elif(add_num[1] > add_num[2] and add_num[1] > add_num[0]):
#     print("Second number is the greatest!")
# else:
#     print("Third number is the greatest!")

# print(add_num)


# num1 :int = int(input("Enter first number: "))

# if(num1 % 7 == 0):
#     print("The number is divisible by 7!")
# else:
#     (print("This number is not divisible by 7!"))


# name : str = "wajid"

# name = "amir"

# print(name)

# data_list : list = []

# data_list.append(input(" Enter your Movie 1 "))
# data_list.append(input(" Enter your Movie 2 "))
# data_list.append(input(" Enter your Movie 3 "))



# print(data_list)



# list1 : list = [1, 2, 3, 2, 1]

# if list1.copy() == list1[::-1]:
#     print("Palindrome")
# else:    print("Not Palindrome")


# grade : list = ("A", "B", "F", "D", "E","C")

# list(grade)

# grade.sort()

# print(grade)




# names : dict = {"name1": "Wajid", "name2": "Amir","name3": "Ali",
#                     "marks": {"mark1": 90, "mark2": 80, "mark3": 70}
#                 }

# print(list(names.keys()))

# data : dict = {}

# data.update({"Phy" : input("Enter your physics marks: ")})
# data.update({"Chem" : input("Enter your chemistry marks: ")})
# data.update({"Biology" : input("Enter your biology marks: ")})

# print(data)



# classroom : set = {"Math", "Science", "History", "Math", "Science" , "History"}

# print(len(classroom))



a : int = 100

while a > 1:
    a = a - 1
    print(a)

name : str = input("Enter your name: ")
print("hellow")