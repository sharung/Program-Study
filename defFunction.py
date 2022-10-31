# def greet(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")

# greet(location = "indonesia",name = "jono")


# # Area Calc
# #Write your code below this line 👇
# import math

# def paint_calc(height, width, cover):
#     num_cans = (height * width) / cover
#     print(f"{math.ceil(num_cans)} ")
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# # check prime number
# def prime_number(number): # function for check prime number
#     as_prime = True # parameter stop
#     for i in range(2, number): # loop for number
#         if number % i == 0 : # condition
#             as_prime = False # ganti parameter to False
#     if as_prime: # it's true than
#         print("It's prime number")
#     else: # it's false
#         print("It's not prime number")

# n = int(input("Check this number : "))
# prime_number(number=n)


# caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def ceasar(start_direction, plain_text, shift_amount):
    new_text = ""
    if start_direction == "decode":
        shift_amount *= -1
    for latter in plain_text:
        position = alphabet.index(latter)
        new_latter = position + shift_amount
        new_text += alphabet[new_latter]
    print(f"The {start_direction}d text is {new_text}")


# def encrypt(plain_text, shift_amount):
#     new_latter = ""
#     for i in plain_text:
#         position = alphabet.index(i)
#         new_position = position + shift_amount
#         new_latter += alphabet[new_position]
#     print(f"The encoded text is {new_latter}")
# def descrypt(plain_text, shift_amount):

ceasar(start_direction=direction, plain_text=text, shift_amount=shift)
