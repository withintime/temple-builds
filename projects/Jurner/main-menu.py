# main-menu.py
# Auto-generated starter file


def startJournal():
    print("Starting Journal...")

def changeCategory():
    print("Changing category...")

def viewLogs():
    print("Viewing logs...")

def settings():
    print("Opening settings...")

def exitProgram():
    print("Goodbye!")
    exit()

# menu text and corresponding functions



def numberedMenu(options):
    while True:
        for i, (option, _) in enumerate(options, 1): # enumerate returns a pair (index, value) == (i, option)
            print(f"[{i}] {option}")
        
        choice = input("> ")
        if choice.isdigit(): # check if input is a digit
            index = int(choice) - 1 # convert it to an int and subtract 1 as a list index starts from 0 in Python
            if 0 <= index < len(options): # check if the input number isn't too high
                return index # return index for future reference - starting new functions for example
        print("Invalid input. Please enter a number from the list.")        

# menu text and corresponding functions
mainMenu = [
    ("Start Journal", startJournal),
    ("Add or Change Category", changeCategory),
    ("View Logs", viewLogs),
    ("Settings", settings),
    ("Exit", exitProgram)
]

if __name__ == "__main__":
    from pyfiglet import figlet_format
    print(figlet_format("Jurner", font="larry3d"))
    choice = numberedMenu(mainMenu)
    mainMenu[choice][1]() # run the function from mainMenu according to the choice