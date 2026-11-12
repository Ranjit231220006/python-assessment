def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice: ")

if choice == "1":
    print("Result:", add(a, b))

elif choice == "2":
    print("Result:", subtract(a, b))

elif choice == "3":
    print("Result:", multiply(a, b))

elif choice == "4":
    if b != 0:
        print("Result:", divide(a, b))
    else:
        print("cannot divide by zero.")

else:
    print("invalid choice")
