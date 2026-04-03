# species = input("Enter your pet species : ")
# age  = int(input("Enter pet age : "))


# if species == "dog" :
#     if age < 2:
#         feed = "Puppy food"

# elif species == "cat" :
#     if age > 5 :
#         feed = "Senior cat food"

# else:
#     feed = "Regular food"
# print("Your species food is :", feed)


species = input("Enter your pet species : ")
age  = int(input("Enter pet age : "))


if species == "dog" and age < 2:
      print("Puppy food")
  

elif species == "cat" and age > 5:
    print("senior cat food")

else:
    print("Regular food")

