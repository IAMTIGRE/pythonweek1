# -------- Program 1 --------
name = input("Enter your name: ")
print("Hello", name)

# -------- Program 2 --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum =", sum)
# -------- Program 3 --------
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x, y = y, x
print("After swapping: x =", x, "y =", y)
# -------- Program 4 --------
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)
# -------- Program 5 --------
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
# -------- Program 6 --------
num = int(input("Enter a number: "))
for i in range(1, 6):
    print(num, "x", i, "=", num*i)
# -------- Program 7 --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
total = a + b + c
print("Total =", total)
# -------- Program 8 --------
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Not positive")
# -------- Program 9 --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
# -------- Program 10 --------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old")