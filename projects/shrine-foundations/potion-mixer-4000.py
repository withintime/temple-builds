# potion-mixer-4000
import random

def greetingsWizard():
    print('~~~ Welcome Wizard! ~~~')

greetingsWizard()

def chooseCastingMethod():
    print('Choose your casting method... (Air / Earth / Fire)')

    while True:
        casting = input().lower()
        if casting not in {'air', 'earth', 'fire'}:
            print("Invalid input! Choose Air, Earth, or Fire.")
            continue
        print(f"You have chosen the path of {casting.capitalize()}.")
        return casting

casting = chooseCastingMethod()

def ingredientsInput(resourceName, stock):
    while True:
        print(f"How much {resourceName} do you want to put in?")
        try:
            amount = float(input())
        except ValueError:
            print("That's not a number you sneak!")
            continue
        if amount > stock:
            print(f"You wish! You don't have that much {resourceName} Your stock is {stock}!")
            continue
        print(f"You put in {amount} {resourceName} and you've got {stock - amount} left.")
        return amount

mana_stock = 1000
essence_stock = 800
souls_stock = 3

mana = ingredientsInput("mana", mana_stock)
essence = ingredientsInput("essence", essence_stock)
souls = ingredientsInput("souls", souls_stock)

def statCalculation(mana, essence, souls):
    while True:
        power = (mana * 1.5 + essence * 2 + souls * 10) ** 1.1
        cost = mana * 2 + essence * 4 + souls * 25
        
        if power / cost < 2:
            print("Potion is ... stable!")
            
            # CRITICAL BREW (10% chance)
            if random.randint(1, 10) == 1:
                print("Congrats! You brewed a critical potion!")
                power *= 2
                cost /= 2
            return(power, cost)
               
        else:
            print("You are too greedy! Potion is not stable and might kill the user! Try again!")
            continue


power, cost = statCalculation(mana, essence, souls)
print(f"Your potion has {power:.2f} power and costs {cost:.2f} cornbreads.")

def promptYesNo(question):
    while True:
        answer = input(question + " (Y/N): ").lower()
        if answer in {'y', 'yes'}:
            return True
        elif answer in {'n', 'no'}:
            return False
        else:
            print("Speak clearly, wizard. Y or N?")

def handleSelling(casting, cost, power):
    if not promptYesNo("Do you want to sell your potion?"):
        print("You stash your potion. Greed... suppressed.")
        return

    if power > 1000:
        buyer_casting = random.choice(['air', 'earth', 'fire'])
        if buyer_casting == casting:
            print(f"A wealthy {buyer_casting.capitalize()} mage gasps at your brew!")
            if promptYesNo("They offer double the price. Do you accept?"):
                print(f"You sold the potion for {cost * 2:.2f} cornbreads!")
            else:
                print("They scoff and vanish into the mist.")
        else:
            print("The mage sniffs, unimpressed. You get 7 blades of grass 🌿.")
    elif power > 500:
        print("A shady rogue offers you 100 cornbreads or eternal curses.")
        if promptYesNo("Do you accept the 100 cornbreads?"):
            print("A fair deal. No curses today.")
        else:
            print("He throws in an extra curse for good measure.")
    else:
        print("No one wants it. A goat nibbles your potion scroll.")

handleSelling(casting, cost, power)