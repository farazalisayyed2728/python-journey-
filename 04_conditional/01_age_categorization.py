age  = int(input("Enter your age : "))
if age < 13:
    print("Child")

elif age == 13 or age <= 19:
    print("Teenager")

elif age == 20 or age <= 59:
    print("Adult")

else:
    print("senior")

