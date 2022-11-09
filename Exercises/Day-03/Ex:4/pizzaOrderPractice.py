# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    price1 = 15
    if add_pepperoni == "Y":
        price1 += 2
        if extra_cheese == "Y":
            price1 += 1
        else:
            price1 += 0
    else:
        price1 += 0
        if extra_cheese == "Y":
            price1 += 1
        else:
            price1 += 0
    print(f"Your final bill is: ${price1}.")
elif size == "M":
    price2 = 20
    if add_pepperoni == "Y":
        price2 += 3
        if extra_cheese == "Y":
            price2 += 1
        else:
            price2 += 0
    else:
        price2 += 0
        if extra_cheese == "Y":
            price2 += 1
        else:
            price2 += 0
    print(f"Your final bill is: ${price2}.")
else:
    price3 = 25
    if add_pepperoni == "Y":
        price3 += 3
        if extra_cheese == "Y":
            price3 += 1
        else:
            price3 += 0
    else:
        price3 += 0
        if extra_cheese == "Y":
            price3 += 1
        else:
            price3 += 0
    print(f"Your final bill is: ${price3}.")
