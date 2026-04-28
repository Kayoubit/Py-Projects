import os

cars = ["Ford", "Volvo", "BMW"]
#y = len(cars)

def prompt(display="Press enter to continue.", require=False):
    if require:
        s = False
        while not s:
            s = input(display + " ")
    else:
        s = input(display + " ")
    return s


def shop():
    while True:
        y = len(cars)
        print("I have a list of cars here. There are " + str(y) + " cars total,\nand they are:")
        for index, value in enumerate(cars):
            print(str(index + 1) + '. ' + value)
#        print(str(len(cars)))
        
        print("\n")
        b = input("Now here are a few options:\n1. Change a car from the list by typing 'change'.\n2. Add a new car by typing 'add'.\n3. Quit the simulation by typing 'quit'.\n\nWhat would you like to do? ")
        if b == "change":
            c = input("\n\nPlease select the car you wish by its designated number. " )
            a = cars[int(c) - 1]
            os.system('cls')
            print("Cool, you have selected " + str(a) + ". Good choice!")
            d = input("\nWhat would you like to change the " + str(a) + " to? ")
            cars[int(c) - 1] = d
            print("\nI have now changed the car you selected. Here is the new list:")
            for index, value in enumerate(cars):
                print(str(index + 1) + '. ' + value)
            #for x in cars:
                #print(x)
            e = input("Would you like to 'continue' with the simulation or 'quit'? ")
            if e == 'continue':
                #print("\n" * 50)
                os.system('cls')
            elif e == 'quit':
                break
        elif b == "add":
            os.system('cls')
            e = input("Ok, then lets add a new car.\nWhat car would you like to add? ")
            cars.append(e)
            print("\nI have now added the car you specified. Here is the new list:")
            for index, value in enumerate(cars):
                print(str(index + 1) + '. ' + value)
            print('\n')
            prompt()
            os.system('cls')
#            print("------------------------------------------------------------------")
#            print('\n' * 10)
        else:
            if b == 'quit':
                break

shop()
