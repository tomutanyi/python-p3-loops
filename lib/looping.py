#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")
# code goes here!
pass

def square_integers(int_list):
    new_list = []
    for i in int_list:
        new_list.append(i ** 2)
    return new_list
    # code goes here!
    pass

def fizzbuzz():
    for i in range (1,101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

    # code goes here!
