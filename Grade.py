#Accept the percentage from the user and display the grade according to the given percentage.
percentage=float(input("Enter the percentage of the student:"))
if 100 >= percentage >= 90:
     print("A+")
elif 90 > percentage >= 80:
    print("A")
elif 80 > percentage >= 70:
    print("B")
elif 70 > percentage >= 60:
    print("C")
elif 60 > percentage >= 50:
    print("D")
elif 50 > percentage >= 0:
    print("F")
else:
    print("Invalid Percentage")