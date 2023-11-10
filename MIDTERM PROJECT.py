import time  # imports time module
from datetime import date  # imports date from datetime module
datecurrent = date.today()  # Sets the variable datecurrent as the date today
adminconsole = f"""-----------[PYRITE ADMIN CONSOLE]-----------
----------------[1]-[STATUS]----------------
----------------[2]-[INBOX]-----------------
----------------[3]-[CREDITS]---------------
----------------[0]-[EXIT]------------------
----------------[{datecurrent}]----------------"""
inbox = """-----------------[INBOX]--------------------
--------------[1]-[MANAGEMENT]--------------
--------------[2]-[ENGINE-BAY]--------------
--------------[3]-[MURDOCK]-----------------
-[0]-[RETURN]-------------------------------"""
sysconsole = f"""----------[PYRITE SYSTEMS CONSOLE]----------
----------------[1]-[LOGIN]-----------------
----------------[2]-[EXIT]------------------
---------------[{datecurrent}]-----------------"""
# The UI, not going to comment on every one of them. f and {datecurrent} formats datecurrent into the UI


def sleep():
    time.sleep(1)
# Function for making the program wait 1(one) second.


print(sysconsole)
# prints the system console UI
while True:  # while true loop
    while True:  # nested while true loop
        response = input("INPUT: ")  # User Input
        if response == "1":
            sleep()
            break
        elif response == "2":
            exit()  # Stops the execution
        else:
            print("---INVALID INPUT---")
    break  # Breaks us out of the nested while loop
print("-------------[INPUT USERNAME]---------------")
while True:
    response = str(input("INPUT: "))
    if response.lower() == "admin":
        sleep()
        break
    else:
        print("--------------[INVALID USER]----------------")
print("-------------[INPUT PASSWORD]---------------")
while True:
    response = input("INPUT: ")
    if response == "12345678":
        sleep()
        sleep()
        print("-------------[ACCESS GRANTED]---------------")
        sleep()
        break
    else:
        print("------------[INVALID PASSWORD]--------------")

while True:
    while True:
        print(adminconsole)  # The admin console from the start, there are selections there
        response = input("INPUT: ")
        if response == "1":  # Selection #1, Ship status
            sleep()
            while True:  # A nested nested while loop
                print("---------------[SHIP STATUS]----------------\n"
                      "-------------[COOLANT == LOW]---------------\n"
                      "-------------[DOCKING == DOCKED]------------\n"
                      "-------------[CREW-BAY == ??#$%^4303948583]-\n"
                      "-------------[BRIDGE == OBSTRUCTED]---------\n"
                      "-[0]-[RETURN]-------------------------------")
                response = input("INPUT: ")
                if response == "0":  # Selection for returning to the menu
                    break

        elif response == "2":  # Selection #2, Inbox
            sleep()
            while True:
                print(inbox)
                response = input("INPUT: ")
                if response == "1":
                    while True:
                        print("-HQ HAS REQUESTED THAT ANY WORD OF THE \"VIRAL\" OUTBREAK--\n"
                              "-IN THE MED-BAY BE SILENCED AT ANY COST... -MANAGEMENT-----\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = input("INPUT: ")
                        if response == "0":
                            break
                elif response == "2":
                    while True:
                        print("-THIS IS ENGINEER M.DOC SPEAKING... WE ARE EXPERIENCING----\n"
                              "-A SEVERE OUTBREAK OF THE POX, ALL OF OUR ENGINE CREW------\n"
                              "-ARE IN A SEVERE STATE OF DECOMMISSION... REQUESTING-------\n"
                              "-ENTRY INTO MEDBAY ASAP -M.DOC-----------------------------\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = input("INPUT: ")
                        if response == "0":
                            break
                elif response == "3":
                    while True:
                        print("-WE NEED AID, PLEASE... I HAVE A FAMI----------------------\n"
                              "-[0]-[RETURN]----------------------------------------------")
                        response = input("INPUT: ")
                        if response == "0":
                            break
                elif response == "0":
                    break

        elif response == "3":  # Selection #3, Credits
            sleep()
            while True:
                print("------------------[CREDITS]-----------------\n"
                      "-[LEAD-DEVELOPER]-[SALVADOR]----------------\n"
                      "--------------------------------------------\n"
                      "-[0]-[RETURN]-------------------------------\n")
                response = input("INPUT: ")
                if response == "0":
                    break
        elif response == "0":  # Selection #4(0), Exit()
            while True:  # To make a "Are you sure? Y/N" popup
                print("------------[ARE YOU CERTAIN?]--------------\n"
                      "---------------[Y]-----[N]------------------")
                response = input("INPUT: ")
                if response.lower() == "y":
                    exit()
                elif response.lower() == "n":
                    break
