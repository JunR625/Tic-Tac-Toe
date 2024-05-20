import random

#Create a list that will be used to store options that are selected by user and random module
options = ["-", "-", "-", 
            "-", "-", "-",
            "-", "-", "-"]

#Assign roles to player and computer
Player = "O"

#Assign True to rungame to a variable. This variable is used to keep game going until a player wins
rungame = True

#Make counter for total moves made
moves = 1

#Prints grid of the game
def printgrid(options):
        print("=========")
        print(options[0] + " | " + options[1] + " | " + options[2])
        print("---------")
        print(options[3] + " | " + options[4] + " | " + options[5])
        print("---------")
        print(options[6] + " | " + options[7] + " | " + options[8])
        print("=========")
        print()

#Prompt user for input and make sure input is in digits and not alphabet(E.g: one, two, three)
def playerinput():
        global row
        global column
        print("To imprint your answer, state the row and column of the '-' you select.")
        row=input("In which row is your 'O'? ")
        column=input("In which colum is your 'O'? ")
        while not row.isdigit():
                print()
                print("Error, please input in digits.")
                row=input("In which row is your 'O'? ")
        while not column.isdigit():
                print()
                print("Error, please input in digits.")
                column=input("In which column is your 'O'? ")



#Keep prompting user for row and column inputs when selected option(-) in grid is not free
def emptyspace(options):
    global row
    global column

    if row == "1":
        while column == "1" and options[0] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "2" and options[1] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "3" and options[2] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
    if row == "2":
        while column == "1" and options[3] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "2" and options[4] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "3" and options[5] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
    if row == "3":
        while column == "1" and options[6] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "2" and options[7] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")
        while column == "3" and options[8] != "-":
            print()
            printgrid(options)
            print("Error, that space is occupied")
            print("To imprint your answer, state the row and column of the # you select.")
            row=input("In which row is your 'O'? ")
            column=input("In which column is your 'O'? ")

#Keep prompting user for row and column inputs when selected inputs(row and columns) are greater than maximum
def maxinput():
    global row
    global column
    while int(row) > 3 or int(column) > 3 or int(row) <= 0 or int(column) <= 0:
        print()
        printgrid(options)
        print("Error, maximum number of rows and columns is 3")
        print("To imprint your answer, state the row and column of the # you select.")
        row=input("In which row is your 'O'? ")
        column=input("In which column is your 'O'? ")

#Assign coordinates(row and columns) to each option on the board if an option(-) on grid is free.
def assign(options):
    global Player
    if row == "1":
            if column == "1" and options[0] == "-":
                    options[0] = Player
            if column == "2" and options[1] == "-":
                    options[1] = Player
            if column == "3" and options[2] == "-":
                    options[2] = Player
    if row == "2":
            if column == "1" and options[3] == "-":
                    options[3] = Player
            if column == "2" and options[4] == "-":
                    options[4] = Player
            if column == "3" and options[5] == "-":
                    options[5] = Player
    if row == "3":
            if column == "1" and options[6] == "-":
                    options[6] = Player
            if column == "2" and options[7] == "-":
                    options[7] = Player
            if column == "3" and options[8] == "-":
                    options[8] = Player




#Check for horizontal wins
def checkhorizontal():
    if options[0] == options[1] == options[2] and options[0] != "-":
        print("Game Over!", Player , "wins!!")
        return True
    elif options[3] == options[4] == options[5] and options[3] != "-":
        print("Game Over!", Player , "wins!!")
        return True
    elif options[6] == options[7] == options[8] and options[6] != "-":
        print("Game Over!", Player , "wins!!")
        return True

#check for vertical wins
def checkvertical():
    if options[0] == options[3] == options[6] and options[0] != "-":
        print("Game Over!", Player , "wins!!")
        return True
    elif options[1] == options[4] == options[7] and options[1] != "-":
        print("Game Over!", Player , "wins!!")
        return True
    elif options[2] == options[5] == options[8] and options[2] != "-":
        print("Game Over!", Player , "wins!!")
        return True

#Check for diagonal wins
def checkdiagonal():
    if options[0] == options[4] == options[8] and options[0] != "-":
        print("Game Over!", Player , "wins!!")
        return True
    elif options[2] == options[4] == options[6] and options[2] != "-":
        print("Game Over!", Player , "wins!!")
        return True

#Check if any player wins
def checkwin():
        global rungame
        if checkdiagonal() or checkvertical() or checkhorizontal():
                return True

#Check for tie
def checktie():
    global rungame
    if "-" not in options:
        print("Game over, its a tie!")
        return True

# switch player
def switchPlayer():
    global Player
    if Player == "O":
        Player = "X"
    else:
        Player = "O"

#Computer's move
def computer(options):
    global crow
    global ccolumn
    while Player == "X":
        position = random.randint(0, 8)
        if options[position] == "-":
            options[position] = "X"
        #determine rows and columns of computer's position for logging
            if position == 0:
                crow = 1
                ccolumn = 1
            elif position == 1:
                crow = 1
                ccolumn = 2
            elif position == 2:
                crow = 1
                ccolumn = 3
            
            elif position == 3:
                crow = 2
                ccolumn = 1
            elif position == 4:
                crow = 2
                ccolumn = 2
            elif position == 5:
                crow = 2
                ccolumn = 3

            elif position == 6:
                crow = 3
                ccolumn = 1
            elif position == 7:
                crow = 3
                ccolumn = 2
            elif position == 8:
                crow = 3
                ccolumn = 3

            switchPlayer()

def playerlog():
    global moves
    log=open("logfile_testing.txt", "a")
    log.write(f"{moves}, P, {row}, {column}, O \n")
    log.close()
    moves += 1

def computerlog():
    global moves
    log=open("logfile_testing.txt", "a")
    log.write(f"{moves}, C, {crow}, {ccolumn}, X \n")
    log.close()
    moves += 1
    
        

"""                                                 ~ Call functions here ~                                                    """


start = input("This is a tic tac toe game. Would you like to start the game? Y/N ").capitalize()
while start == "Y":
        while rungame:
            printgrid(options)  #Print grid of the game
            playerinput()       #Prompt player for input
            maxinput()          #Make sure input is not bigger than number of rows and columns available
            emptyspace(options) #Make sure selected answer is available and not already chosen by computer or user
            assign(options)     #After errors are handled, assign input answer to list
            playerlog()

            printgrid(options)  #print grid again to let user visualize result
            if checkwin(): break     #if checkwin function returns true, break this inner loop
            elif checktie(): break   #else, if checktie function returns true, break this inner loop

            switchPlayer()
            computer(options)
            computerlog()
               
            if checkwin(): break
            elif checktie(): break

        #After game is over, prompt user to restart game
        start = input("Would you like to restart the game? Y/N ").capitalize()
        if start == "Y":
                options.clear()         #Reset the grid options
                options = ["-", "-", "-", 
                           "-", "-", "-",
                           "-", "-", "-" ]
                moves = 1               #Reset moves counter to one
                rungame = True          #Set rungame to true so game would loop again
