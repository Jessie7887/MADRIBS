
import game

# describes (with examples) the part of speech in the english language
# noun, verb, pronoun, properNoun, adjective, adverb, preposition, conjunction
def learn():
    print("Noun - person, place, or thing.")
    print("Example: car, bus, egg\n\n")

    print("Verb - shows action, state occurrence; forms main part of the predicate of a sentence")
    print("Example: looks, types, laughs\n\n")
    
    print("Pronoun - person, place thing; stands in for noun to avoid repetative use of noun")
    print("Example: she, her, him. they\n")

    print("Proper Noun - name given to an individual person, place, or thing; usually starts with a capital letter")
    print("Example: Jessie, Japan, Linux \n\n")

    print("Adjective - modifies or describes something (such as a noun)")
    print("Example: shiny, lightweight, sweet\n\n")

    print("Adverb - modifies or qualifies an adjective, verb, or noun; expresses a relational connection of time, place, degree, etc")
    print("Example: brightly, quietly, sweetly\n\n")

    alldone = input("Press X when you are done reading & ready to play.  ")
    if alldone == "X":
        game.start()


