# Read three angles of triangles and determine their types (Right triangle, Obtuse triangle, Acute triangle).
m1=int(input("Enter the value of first angle:"))
m2=int(input("Enter the value of second angle:"))
m3=int(input("Enter the value of third angle:"))
if m1+m2+m3==180 and(m1<90 or m2<90 or m3<90):
    print("The given triangle is a acute triangle.")
elif m1+m2+m3==180 and(m1==90 or m2==90 or m3==90):
    print("The given traingle is a right triangle.")
else:
    print("The given triangle is an obtuse triangle.")
    
