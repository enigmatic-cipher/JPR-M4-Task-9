"""
Given a char as input, print Apple if it is A, Boy if it is B, Cat if it is C and None otherwise.
Input-> C
Output-> Cat
"""

def char_1(ch):

  if ch == "A":
    print("Apple")
  
  elif ch == "B":
    print("Boy")

  elif ch == "C":
    print("Cat")

  else:
    print("None")

alp = input("Enter Alphaber: ")

char_1(alp)
