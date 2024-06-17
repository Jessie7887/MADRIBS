# category1 >> friends & family

import GetterPOS
import time


def prompt1():
    # I have a {noun} named {Proper Noun}. {Pronoun} likes to eat {noun s/p},
    # but not on {Day of The Week}.

    # use alphabetical call order for inputs
    print("Here is your ML from the category: Friends & Family.\n")
    a = GetterPOS.getnoun()
    b = GetterPOS.getProperNoun()
    c = GetterPOS.getpronoun()  # get 1st letter of this input to be capital
    # print("Note, the next one can be singular or plural.")
    d = GetterPOS.getnoun()
    day = input("Enter a day of the week: ")  # special condition

    # Funny reading time
    print("Well Done! Ready to read your story?")
    time.sleep(3)
    p1Ending = f"I have a {a} named {b}. {c} likes to eat {d}(s), but not on {day}s."
    print(p1Ending)
    exit(0)


def prompt2():
    # {noun} taste(s) good especially when paired with {deli meat}. {SAMEpronoun} should {verb} them sometime if 
    # {SAMEpronoun} ever feel {verb}. Napkins, salami, you, try, you, adventurous use alphabetical call order for inputs
    print("Here is your ML from the category: Friends & Family.\n")
    a = GetterPOS.getnoun()
    meat = input("Enter a deli meat: ")  # special condition
    print("The next entry will be used twice in this category, Chose wisely ;)")
    b = GetterPOS.getpronoun()
    c = GetterPOS.getverb()
    d = GetterPOS.getverb()

    print("Well Done! Ready to read your story?")
    time.sleep(3)
    p2Ending = f"{a} taste(s) good especially when paired with {meat}. {b} should {c} them sometime if {b} ever feel {d}."
    print(p2Ending)
    exit(0)


def prompt3():
    # Finally, a prompt that makes sense. Let's talk about family, and friends -- the family you choose.
    # Isn't it wonderful that in the whole wide *world there's only a select few that make you heart burst with joy?

    print("Here is your ML from the category: Friends & Family.\n")
    a = GetterPOS.getnoun()
    b = GetterPOS.getverb()  # get 1st letter of this input to be capital
    c = GetterPOS.getnoun()
    d = GetterPOS.getverb()
    e = GetterPOS.getadjective()
    f = GetterPOS.getnoun()
    organ = input("Enter the name of an organ: ")
    g = GetterPOS.getverb()

    print("Well Done! Ready to read your story?")
    time.sleep(3)
    p3Ending = f"Finally, a {a} that makes sense. Let's {b} about family, and friends -- the {c} you {d}. " \
               f"Isn't it {e} that in the whole wide *{f} there's only a select few that make your {organ} {g}" \
               f" with joy?"
    print(p3Ending)
    exit(0)


