#specify a secret word, thats stored inside the program and user can interact and gues the secret word
secret_word = "Giraffe"
guess = " " #empty string to store users response
#need to prompt the user to input the secret word and also later prompt again
#cant use simple input statements but also while loop
while guess != secret_word:
     guess = input("Enter your guess:")

print("You guessed it right!")

#now make the same game with the number of guesses be controlled
#making a new variable n_guess and adding it as additional condition to while loop:
n_guess = 0
while n_guess <=3 and guess != secret_word:
     guess = input("Enter your guess:")
    