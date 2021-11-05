def add(x, y):
   return x + y
def sub(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y): 
   return x / y
print("Select operation.")
print("+.Add")
print("-.Subtract")
print("*.Multiply")
print("/.Divide")
option = input("Enter operator:")
num1 = int(input("Enter number: "))
num2 = int(input("Enter second number to continue calculation: "))
if option == '+':
   print(num1,"+",num2,"=", add(num1,num2))
elif option == '-':
   print(num1,"-",num2,"=", sub(num1,num2))
elif option == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif option == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Incorrect input")