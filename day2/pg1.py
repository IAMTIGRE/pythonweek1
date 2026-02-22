try:
    num=float(input("Enter a number: "))
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")
except ValueError:
    print("Kindly enter a valid integer.")