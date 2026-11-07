num1 = float(input("What is your first number?   "))
operation = int(input("What is the operarion you would like to use?\n \n 1.Addition  \n2.Subtraction \n3.Multiplication \n4. Division\n5.Power \n6.Modulus\n7.Floor Division\n\n"))
num2 = float(input("\n\nWhat is your second number? "))
if operation == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == 5:
    print(f"{num1} to the power of {num2} is {num1 ** num2}")
elif operation == 6:
    print(f"{num1} divide by {num2} with remainder is {num1 % num2}")
elif operation == 7:
    print(f"{num1} // {num2} = {num1 // num2}")