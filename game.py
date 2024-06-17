

import PartsOfSpeech
import Choose
import time
# the gaaaaaame
# Order: Welcome(in main), LEarn teh parts of speech(POS), choose a category

def rules():
    print("\nThis is mAd libs, or I as like to call it, mAD RiBS.\n")
    time.sleep(2)
    print("Come prepared with grammar knowledge (or not) & create a funny story")
    print("Follow the on-screen prompts to type in the correct parts of speech or specific type of word (example: day "
          "of the week, dog breed, etc) to create the story.\n")
    time.sleep(2)
    print("You will get the choose your story category to help you come up with words.")
    print("Available today we have these Categories: Friends & Family, Computers.\n")
    time.sleep(5)
    print("Within those categories are the prompts, which again is your choice.\n")
    print("There are 2-3 story prompts in each category.\n")
    time.sleep(2)

def gotime():
    print("\nEnough chit chat. are you ready to play??")
    time.sleep(2)
    go = input("yay or ney: ")
    if go == "yay":
        play()
    if go == "ney":
        print("There's only 1 right answer :/")
        sure = input("Are you sure you wanna leave? Y/N: ")
        if sure == "Y":
            exit(0)
        elif sure == "N":
            print("Good >:)")
            play()

def play():

    print("Before we begin, would you like to view the English Parts Of Speech?")
    learn = input("Y/N ")
    if learn == "Y":
        PartsOfSpeech.learn()
    elif learn == "N":
        print("Alright then.\n")
        start()
    else:
        print("bruh")



def start():
    # launches game (by means of choose>category.prompt>game)
    Choose.choice()



