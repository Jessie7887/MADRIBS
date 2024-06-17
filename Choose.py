

import Friends_and_Family
import Computers
# Chooses what category you want to play ML, then choose a prompt
# each category has 2-3 prompts

# category choices <-- Start here
def choice():
    # pick = input("Choose a category...\n* F&F\n* Comp\n>> ")m
    while True:
        pick = input("Choose a category...\n* F&F\n* Comp\n>> ")
        if pick == "F&F":
            choiceFF()
        if pick == "Comp":
            choiceComp()
        # if pick == "NO":
        #     choiceNO()



# prompt choices from F&F
def choiceFF():
    select = input("Choose a prompt: \n* Prompt 1\n* Prompt 2\n* Prompt 3\n>> ")
    while True:
        # 1 or 2
        if select == "Prompt 1":
            # Choose Prompt 1 from Category: Friends & Family
            Friends_and_Family.prompt1()
        if select == "Prompt 2":
            # Choose Prompt 2 from Category: Friends & Family
            Friends_and_Family.prompt2()
        if select == "Prompt 3":
            # Choose Prompt 3 from Category: Friends & Family
            Friends_and_Family.prompt3()
        else:
            select = input("Choose a prompt: \n* Prompt 1\n* Prompt 2\n* Prompt 3\n>> ")

# prompt choices from Comp
def choiceComp():
    select = input("Choose a prompt: \n* Prompt 1\n* Prompt 2\n* Prompt 3\n")
    while True:
        # 1 or 2
        if select == "Prompt 1":
            # Choose Prompt 1 from Category: Friends & Family
            Computers.prompt1()
        if select == "Prompt 2":
            # Choose Prompt 2 from Category: Friends & Family
            Computers.prompt2()
        if select == "Prompt 3":
            # Choose Prompt 3 from Category: Friends & Family
            Computers.prompt3()


## we'll add more :)
# def choiceNO():
#     pass

