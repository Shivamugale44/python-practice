a=10
b=21
if(a>b):
    print(" a is grater tahn b")
else:
    print("b is greter than a")
    #add and sub
x=10
y=5
z=x+y   
print("addition of x and y is:",z)
z=x-y   
print("subtraction of x and y is:",z)
z=x*y
print(" multiplication of x and y is:",z)    
z=x/y
print("division of x and y is:",z)
# table of 5
a=int(input("enter the number for table:")) 
for i in range(1,11):
    print(a,"*",i,"=",a*i)
##### 2to 10 table
for num in range(2, 21):
    print("Table of", num)  
    for i in range(1, 11):
        print(num, "*", i, "=", num * i)
    print()  # Print a blank line after each table  
# year check
year=int(input("enter the year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")