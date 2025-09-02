# WAP to check if the last digit is 4.
num = int(input("Enter a number: "))
lastdigit = num % 10
if (lastdigit == 4):
    print("The last digit is 4.")
else:
    print("The last digit is not 4.")
