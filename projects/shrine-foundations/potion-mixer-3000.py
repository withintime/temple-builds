# Potion Mixer 3000
import random

# resources to start
mana_stock = 1000
essence_stock = 800
souls_stock = 3

print('Welcome to potion mixer 3000!')

# casting method
print('Choose your casting method... (Air / Earth / Fire)')

casting = input().lower()

if casting not in {'air', 'earth', 'fire'}:
    print("Invalid input! Choose Air, Earth, or Fire.")
    exit()
else:
    print(f"You have chosen the path of {casting.capitalize()}.")

# ingredients input
print('How much mana do you want to put in?')
mana = float(input())
if mana > mana_stock:
    print('Your mana stock is lower than that!')
    exit()
else:
    print(f"You put in {mana}, you got {mana_stock - mana} left.")
print('How much essence do you want to put in?')
essence = float(input())
if essence > essence_stock:
    print('Your essence stock is lower than that!')
    exit()
else:
    print(f"You put in {essence}, you got {essence_stock - essence} left.")
print('How many souls do you want to put in?')
souls = int(input())
if souls > souls_stock:
    print('Your souls stock is lower than that!')
    exit()
else:
    print(f"You put in {souls}, you got {souls_stock - souls} left.")

# stats calculation
print('Calculating potion power and cost...')
power = (mana ** 2 + essence * 2.5) * 3 - souls / 1.2
cost = (mana * essence) * 3 + souls * 10

if random.randint(1,10) < 9:
    print(f"Your potion is of {power} power and costs {cost} cornbreads.")
    if power / cost < 3:
        print('Your potion is stable!')
    else:
        print('You are too greedy and you die :(')
        exit()
else:
    print(f"You brewed a critical potion! Congrats! \nYour potion is of {power * 2} power and costs {cost/10}")

# naming
name = input("What shall this potion be called, wizard?\n")
print('~~~ bubbling... bubbling... ~~~')
print('(    )')
print(' )  (')
print('(____)')
print(f"{name} has been forged with {power} power...")

# potion rarity
if power > 1500:
    print("🌟 Legendary Potion!")
elif power > 500:
    print("✨ Rare Brew!")
else:
    print("🧪 Common potion.")

# selling logic
print('Do you want to sell your potion? Y / N')
decision = input().lower()
if decision not in {'y', 'yes', 'n', 'no'}:
    print('Why do I even bother... <lightning strikes you down>')
elif decision in {'n', 'no'}:
    print('Okay then, safe travels!')
else:
    castingList = ['air', 'earth', 'fire']
    customer = random.choice(castingList)
    if customer == casting:
        print('Wealthy buyer wants to buy your casting type potion for double the price! Do you accept?')
        decision = input().lower()
        if decision not in {'y', 'yes', 'n', 'no'}:
            print('Why do I even bother... <lightning strikes you down>')
        elif decision in {'n', 'no'}:
            print('Okay then, good choice...')
        else:
            print('Great decision... you sold your soul to the babylon.... hope you are happy')
    else:
        if power > 1500:
            print('I offer you 7 blades of grass! Do you accept?')
            decision = input().lower()
            if decision not in {'y', 'yes', 'n', 'no'}:
                print('Why do I even bother... <lightning strikes you down>')
            elif decision in {'n', 'no'}:
                print('Okay then, safe travels!')
            else:
                print('Great decision... Illusion of free choice huh')
        elif power > 500:
            print('I offer you 7 blades of grass!')
            decision = input().lower()
            if decision not in {'y', 'yes', 'n', 'no'}:
                print('Why do I even bother... <lightning strikes you down>')
            elif decision in {'n', 'no'}:
                print('Okay then, safe travels!')
            else:
                print('Great decision... Illusion of free choice huh')

