#!/usr/local/bin/python3

# Exercise 11: Asking Questions 
# Learn Python the Hard Way by Zed A. Shaw

print ("How old are you? ", end="")
age = input()
print ("How tall are you? ", end="")
height = input()
print ("How much do you weigh? ", end="")
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
