def determinant(a, b, c):
    return b*b-4*a*c

valueA = int(input("What is the Value of the X^2 Coefficient?"))
valueB = int(input("What is the Value of the X Coefficient?"))
valueC = int(input("What is the Value of the constant term?"))

print(determinant(valueA, valueB, valueC))