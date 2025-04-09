def Add():
    sum1 = int(input("Enter first number:"))
    sum2 = int(input("Enter second number;"))
    print("The sum is:", sum1 + sum2)

def Subtract():
    sub1 = int(input("Enter first number:"))
    sub2 = int(input("Enter second number;"))
    print("The subtraction is:", sub1 - sub2)

def Multiply():
    mul1 = int(input("Enter first number:"))
    mul2 = int(input("Enter second number;"))
    print("The multiplication is:", mul1 * mul2)

def Divide():
    div = int(input("Enter first number:"))
    div2 = int(input("Enter second number;"))
    print("The division is:", div / div2)

def Calculator():
    fin = False
    while not(fin):
        opc = int(input("Option:"))
        if (opc == 1):
            Add()
        elif(opc == 2):
            Subtract()
        elif(opc == 3):
            Multiply()
        elif(opc == 4):
            Divide()
        elif(opc == 5):
            fin = 1

print ("""Welcome to the calculator
       
       Menu
       1. Add
       2. Subtract
       3. MUltiply
       4. Divide 
       5. Exit
       """)
Calculator()
# This is a simple calculator program that performs basic arithmetic operations.
