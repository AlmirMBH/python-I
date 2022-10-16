
secret_word = "Bosnia"
guess_limit = 3
guess_no = 0
guess = ""
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_no < guess_limit:
        guess = input("Enter a secret word: ")
        guess_no += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Game over! No more guesses")
else:
    print("You won, the secret word is: " + secret_word)
