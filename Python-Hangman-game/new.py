import random
import hangman_art
import hangman_words

print(hangman_art.logo)
print("")

chosen_word = random.choice(hangman_words.word_list)

display = []

for i in range (0, len(chosen_word)):
    display.append("_")

for char in display:
    print(f"{char} ", end = "")

print("\n\n")


flag = False
lives = 6


while flag != True:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}, please try a different letter!")
        print("")
        
    for i in range (0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
        
    if guess not in chosen_word:
        print(f"You have a guessed {guess}, that is not in the word. You lose a life.")
        print((hangman_art.stages[lives]))
        for char in display:
            print(f"{char} ", end = "")
        lives -= 1
        if lives == -1:
            flag = True
            print(f"\n\nThe word was {chosen_word}")
            print("You lose!")
        
    if guess in chosen_word:
        for char in display:
            print(f"{char} ", end = "")
   
    print("\n\n")
    
    if "_" not in display:
        flag = True
        print("You won!")