from random import randint

bet = randint(100, 999)

print(f"The winning number is {bet}.")

while True:
    user = (input("Hatag Number sa Swertres (three-digit number) STRAIGHT/SCRAMBLE numbers: "))
    if user.isdigit() and len(user) == 3:
        break
    else:
        print("Tulo ra ka number sa Swertres migo.")

if int(user) == bet:
    print("Congratulations! Daug ka sa Swertres.")
elif sorted(user) == sorted(str(bet)):
    print("Congratulations! Daug ka sa SCRAMBLE.")
else:
    print(f"Sorry, pildi ka. The winning number was {bet}.")
