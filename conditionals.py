#if a number is positive
num = input("Enter a number: ")

if num > "0":
    print("Your number is positive")
if num < "0":
    print("Your number is negative")
    
#finding the profit or loss
costprice = int(input("Enter cp: "))
sellingprice = int(input("Enter sp: "))

loss = costprice - sellingprice
profit = sellingprice - costprice
if sellingprice > costprice:
    print("the profit made is", profit)
else :
    print("The loss is", loss)
    
#finding if a number is greater or smaller than 15
i = int(input("Enter a number: "))

if i > 15:
    print(f"{i} is greater than 15")
else :
    print(f"{i} is less than 15")
    
#finding if a number is even or odd
n = int(input("Enter a number: "))

if ( n%2==0 ):
    print(f"{n} is an even value")
else :
    print(f"{n} is a odd value")

#using logical operators we can minimize the lines of code
a = int(input("enter value for a: "))
b = int(input("enter value for b: "))
c = int(input("enter value for c: "))

if a > b:
    print(f"{a} is greater than {b}")
if a > c:
    print(f"{a} is greater than {c}")
if b > a:
    print(f"{b} is greater than {a}")
if b > c:
    print(f"{b} is greater than {c}")
if c > b:
    print(f"{c} is greater than {b}")
if c > a:
    print(f"{c} is greater than {a}")