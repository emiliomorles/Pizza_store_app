# Pizza Order. automatic pizza order program app. 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? small, medium, or large ")
add_pepperoni = input("Do you want pepperoni (+2$ S size and +3$ M and L size)? yes or no ")
extra_cheese = input("Do you want extra cheese (+1$)? yes or no ")

price = 0
if size == "small":
  price += 15
elif size == "medium":
  price += 20
elif size == "large":
  price += 25

# extra_pepperoni +2$ for S and +3$ for M and L   
if add_pepperoni == "yes":
  if size == "small":
    price += 2
  else:
    price += 3
else:
  (f"Your total bill is ${price}")
  
# extra_cheese +1$
if extra_cheese == "yes":
  price += 1

print(f"You choose a {size} pizza. {add_pepperoni} for pepperoni and {extra_cheese} for extra chesse.\n")
print(f"Your total bill is ${price}")