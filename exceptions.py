import sys
try:
    x=int(input("Enter a number : "))
    y=int(input("Enter another number :"))
except ValueError:
    print("Number cannot be a Letter")
    sys.exit(1)

try: 
    result = x/y
except ZeroDivisionError:
    print("Error : Cannot divide by zero")
    sys.exit(1)

print(f"{x}/{y}={result}")
