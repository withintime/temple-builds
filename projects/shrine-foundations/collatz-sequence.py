# collatz sequence

def collatz(number):
    steps = 0
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)
        steps += 1
    print(f'It took {steps} steps')

def promptYesNo(question):
    while True:
        answer = input(question + " (Y/N): ").lower()
        if answer in {'y', 'yes'}:
            return True
        if answer in {'n', 'no'}:
            return False

max_steps = 0
number_with_max = 0

for n in range(1, 100000):
    steps = collatz(n)
    if steps > max_steps:
        max_steps = steps
        number_with_max = n

print(f"Number {number_with_max} took the most steps: {max_steps}")

while True:
    try:
        number = int(input("Input your number: "))
    except ValueError:
        print("That's not a number you sneak!")
        continue
    collatz(number)
    if not promptYesNo("Do you want to try again?"):
        exit()
    

