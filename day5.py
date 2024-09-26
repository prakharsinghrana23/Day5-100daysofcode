fruits = ["Apple", "Peach", "Pear"]
for fruits in fruits:
    print(fruits)
    print(fruits + " pie")
print(fruits)
#Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.
#indentation is improtant


student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))
for student in student_scores:
    print(student)

total_exam_scores=sum(student_scores)
print(total_exam_scores)

#range function with for loop

for number in range (1,11,3):
    print(number)

for number in range (1,101):
    print(number)

total=0
for number in range(1,101):
    total+=number
print(total)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
password = ""
#nr_letters =4
import random
for char in range (1,nr_letters+1):
    #1 -4
    random_char=random.choice(letters)
    password += random_char
    print(password)

for char in range  (1,nr_symbols+1):
    random_char=random.choice(numbers)
    password += random_char
    print(password)

for char in range (1,nr_numbers+1):
    random_char=random.choice(symbols)
    password += random_char
    print(password)

    # hard level

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")
