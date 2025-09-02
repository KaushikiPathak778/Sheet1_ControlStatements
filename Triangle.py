#You are given 3 integer angles of a triangle. Tell whether the triangle is valid or not.
m1=int(input("Enter the value of first angle:"))
m2=int(input("Enter the value of second angle:"))
m3=int(input("Enter the value of third angle:"))
sum=m1+m2+m3
if (sum==180):
   print("Triangle is valid.")
else:
    print("Triangle is not valid.")