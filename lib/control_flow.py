#!/usr/bin/env python3


# value_if_true if condition else value_if_false
def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return 'Access granted'
    else:
        return 'Access denied'

def hows_the_weather(temp):
    if temp < 40:
        res = 'brisk'
    elif temp >= 40 and temp <= 65:
        res = 'a little chilly'
    elif temp > 85:
        res = 'too dang hot'
    else:
        res = 'perfect'
    return "It's "+ res + " out there!"

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num

def calculator(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        print('Invalid operation!')
        return None