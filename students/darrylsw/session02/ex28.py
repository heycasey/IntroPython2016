#!/usr/local/bin/python3

# Exercise 28: Boolean Practice
# Learn Python the Hard Way by Zed A. Shaw

print ("1. True and True")
print ("My answer: True")
print ("Answer:", True and True, "\n")

print ("2. False and True")
print ("My answer: False")
print ("Answer:", False and True, "\n")

print ("3. 1 == 1 and 2 == 1")
print ("My answer: False")
print ("Answer:", 1==1 and 2==1, "\n")

print ("4. \"test\" == \"test\"")
print ("My answer: True")
print ("Answer:", "test" == "test", "\n");

print ("5. 1 == 1 or 2 != 1")
print ("My answer: True")
print ("Answer:", 1 == 1 or 2 != 1, "\n");

print ("6. True and 1 == 1")
print ("My answer: True")
print ("Answer:", True and 1 == 1, "\n");

print ("7. False and 0 != 0")
print ("My answer: False")
print ("Answer:", False and 0 != 0, "\n");

print ("8. True or 1 == 1")
print ("My answer: True")
print ("Answer:", True or 1 == 1, "\n")

print ("9. \"test\" == \"testing\"")
print ("My answer: False")
print ("Answer:", "test" == "testing", "\n")

print ("10. 1 != 0 and 2 == 1")
print ("My answer: False")
print ("Answer:", 1 != 0 and 2 == 1, "\n")

print ("11. \"test\" != \"testing\"")
print ("My answer: True")
print ("Answer:", "test" != "testing", "\n")

print ("12. \"test\" == 1")
print ("My answer: False")
print ("Answer:",  "test" == 1, "\n")

print ("13. not (True and False)")
print ("My answer: True")
print ("Answer:", not (True and False), "\n")

print ("14. not (1 == 1 and 0 != 1)")
print ("My answer: False")
print ("Answer:", not (1 == 1 and 0 != 1), "\n")

print ("15. not (10 == 1 or 1000 == 1000")
print ("My answer: False")
print ("Answer:", not (10 == 1 or 1000 == 1000), "\n")

print ("16. not (1 != 10 or 3 == 4)")
print ("My answer: False")
print ("Answer:", not (1 != 10 or 3 == 4), "\n")

print ("17. not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")")
print ("My answer: True")
print ("Answer:", not ("testing" == "testing" and "Zed" == "Cool Guy"), "\n")

print ("18. 1 == 1 and (not (\"testing\" == 1 or 1 == 0))")
print ("My answer: True")
print ("Answer:", 1 == 1 and ( not ("testing" == 1 or 1 == 0)), "\n")

print ("19. \"chunky\" == \"bacon\" and (not (3 == 4 or 3 == 3))")
print ("My answer: False")
print ("Answer:", "chunky" == "bacon" and (not (3 == 4 or 3 == 3)), "\n")

print ("20. 3 == 3 and (not (\"testing\" == \"testing\" or \"Python\" == \"Fun\"))")
print ("My answer: False")
print ("Answer:", 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")), "\n")
