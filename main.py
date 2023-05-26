print("Welcome to Martínez Pizza Deliveries!")
size = str(input("What size pizza do you want? S, M or L? "))
pepp = str(input("Do you want pepperoni? Yes or No. "))
cheese = str(input("Do you want extra cheese? Yes or No. "))
bill = 0 
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if pepp == "Yes":
  if size == "S":
    bill += 2
  else:
    bill += 3
if cheese == "Yes":
  bill += 1
print(f"Your final bill is ${bill}")
