import math
print("""
-------------------------------------------------------------------------------------------
Pythagorean Theorem calculator! Enter '?' if it's unknown!
Don't use non-numbers or '?'
-------------------------------------------------------------------------------------------
""")
A = input("A length: ")
B = input("B length: ")
C = input("C length: ")

if C == "?":
    combine_like_terms = float(A) ** 2 + float (B) ** 2
    solution = math.sqrt(combine_like_terms)
    print(solution)
    if float(A) ** 2 + float(B) == solution:
        print("This is also a real right triangle!")
    else:
        print("This is not a right triangle!")
elif B == "?":
    combine_like_terms = float(C) ** 2 - float(A) ** 2
    solution = math.sqrt(combine_like_terms)
    print(solution)
    if float(A) ** 2 + float(B) == solution:
        print("This is also a real right triangle!")
    else:
        print("This is not a right triangle!")
elif A == "?":
    combine_like_terms = float(C) ** 2 - float(B) ** 2
    solution = math.sqrt(combine_like_terms)
    print(solution)
    if float(A) ** 2 + float(B) == solution:
        print("This is also a right1 triangle!")
    else:
        print("This is not a triangle!")
elif A and B and C == "?":
    print("Nothing is known!")
elif A and B and C != "?":
    print("Invalid character or too much information!")
exit()



