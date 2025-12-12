import calculator
import gemometry
import greeting

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
greeting.greet("Rohitt")

print("Addition: ",calculator.add(num1,num2))
print("Subtraction: ",calculator.subtract(num1,num2))
print("Multiplication: ",calculator.multiply(num1,num2))

print("Area: ",gemometry.area(num1,num2))
print("Perimeter: ",gemometry.perimeter(num1,num2))