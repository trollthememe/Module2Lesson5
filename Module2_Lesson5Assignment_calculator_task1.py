#Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation.
#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

# defining the functions
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division (x, y):
    if y == 0:          # second number in division can't be zero.
        return "Error: Invalid input. Division by zero is not defined."
    return x / y

operations = {"+": addition, "-": subtraction, "*": multiplication, "/": division} #Setting numbers to operations

print("Select operation: + , - , *, / ") #user interaction
opps = input().strip()

if opps in operations:  
    num1, num2 = map(float, input("Enter two numbers separated by a space: ").split()) # converts string 
    result = operations[opps](num1, num2)
    print(f"{num1} {opps} {num2} = {result}")
else:
    print("Invalid option")
