# for the peeps

import GetterPOS
import time

def bye():
    print("\nThanks for playing! :D")


# UNDER CONSTRUCTION
def prompt1():
    # I need more {noun} on my computer. Maybe I need {number} gigabytes? Or, no maybe 128 {noun}?
    # A new {noun} would also be nice. Hi-speed internet with 800 {noun} per {unit-of-time}.
    # Yeah, that'll be {adjective}. {Conjunction} maybe a keyboard with new {shape} keys.

    # use alphabetical call order for inputs
    print("Here is your ML from the category: Computers.\n")
    a = GetterPOS.getnoun()
    b = GetterPOS.getProperNoun()
    c = GetterPOS.getpronoun()  # get 1st letter of this input to be capital
    # print("Note, the next one can be singular or plural.")
    d = GetterPOS.getnoun()
    day = input("Enter a day of the week: ")  # special condition

    # Funny reading time
    print("Well Done! Ready to read your story?")
    time.sleep(3)
    p1Ending = f"STRINGYSTRINGALONGG1"
    print(p1Ending)
    bye()
    exit(0)



# UNDER CONSTRUCTION
def prompt2():
    # I have a {noun} named {Proper Noun}. {Pronoun} likes to eat {noun s/p},
    # but not on {Day of The Week}.

    # use alphabetical call order for inputs
    print("Here is your ML from the category: Computers.\n")
    a = GetterPOS.getnoun()
    b = GetterPOS.getProperNoun()
    c = GetterPOS.getpronoun()  # get 1st letter of this input to be capital
    # print("Note, the next one can be singular or plural.")
    d = GetterPOS.getnoun()
    day = input("Enter a day of the week: ")  # special condition

    # Funny reading time
    print("Well Done! Ready to read your story?")
    time.sleep(3)
    p2Ending = f"STRING2"
    print(p2Ending)
    bye()
    exit(0)

# UNDER CONSTRUCTION
# def prompt3():
#     # I have a {noun} named {Proper Noun}. {Pronoun} likes to eat {noun s/p},
#     # but not on {Day of The Week}.

#     # use alphabetical call order for inputs
#     print("Here is your ML from the category: Computers.\n")
#     a = GetterPOS.getnoun()
#     b = GetterPOS.getProperNoun()
#     c = GetterPOS.getpronoun()  # get 1st letter of this input to be capital
#     # print("Note, the next one can be singular or plural.")
#     d = GetterPOS.getnoun()
#     day = input("Enter a day of the week: ")  # special condition

#     # Funny reading time
#     print("Well Done! Ready to read your story?")
#     time.sleep(3)
#     p3Ending = f"STRING3"
#     print(p3Ending)
#     bye()
#     exit(0)

