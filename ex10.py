#Python exercise 10
coins = 0

print(f"You have {coins} coin(s).")
want_coin = input("Do you want another, yes or no? ")

while want_coin == "yes":
    coins += 1
    print(f"You have {coins} coin(s).")
    want_coin = input("Do you want another, yes or no? ")
else:
    print("Bye")