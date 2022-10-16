character_name = "Almir"
character_last_name = "Mustafic"
text = "This is a random test text"

is_male = True
if is_male:
 print("IF statement works!\nOr maybe not?")

print("Hi, " + character_name.upper() + ", how are you? Is your last name " + character_last_name.lower() + "?")
print(len(text))
print(text[0])
print(text.index("t"))
print(text.replace("a random", "might be a"))

# Mad libs game
color = input("Enter color: ")
plural_noun = input("Enter plural noun: ")
celebrity = input("Enter celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
