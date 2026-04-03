# movie_ticket_price = 12
# age = int(input("enter your age : "))
# day = input("Whats the day is today ? : ")

# if age > 18 :
#     print("pay 12 dollor for Ticket THANKS. ")
#     if day == "wednesday":
#         print("Pay only 10 dollor only for Ticket THANKS. ")

# elif age < 18 :
#     print("Pay 8 dollor for Ticket THANKS. ")
#     if day == "wednesday":
#         print("Pay only 6 dollor for Ticket THANKS. ")


age = 2
day = "wednesday"

price = 12 if age >= 18 else 8
if day == "wednesday":
    price -= 2

print("TICKET price for you is : ", price)