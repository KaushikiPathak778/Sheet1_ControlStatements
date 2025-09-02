# Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.
num = int(input("Enter a number: "))
if (num % 5 == 0 and num % 11 == 0):
    print("The number is divisible by both 5 and 11.")
else:
    print("The condition is not satisfied.")