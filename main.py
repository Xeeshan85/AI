from src import Hangman
from src import get_word, load_words
import os

WORDLIST_FILENAME = "words.txt"
MAX_GUESSES = 6

words_list_level1,words_list_level2,words_list_level3 = load_words(WORDLIST_FILENAME)

os.system('cls' if os.name == 'nt' else 'clear')
print("<<=============WELCOME TO HANGMAN===================>>")


xflag=False
while True:
    if Hangman.wins < 3:
        secret_word = get_word(words_list_level1)
        print(f"Lets Hang::---------(|LEVEL-{Hangman.levels}|)", secret_word)
    elif 3 < Hangman.wins < 6:
        secret_word = get_word(words_list_level2)
        print(f"Lets Hang::---------(|LEVEL-{Hangman.levels}|)", secret_word)
    else:
        secret_word = get_word(words_list_level3)
        print(f"Lets Hang::---------(|LEVEL-{Hangman.levels}|)", secret_word)
    
    print(f"\nThe word has {len(secret_word)} characters.")
    print("Good luck!")

    hangman = Hangman(secret_word, MAX_GUESSES)
    hangman.play()

    print(f"\nTotal Games: {Hangman.total_games}, Wins: {Hangman.wins}, Losses: {Hangman.total_games - Hangman.wins}")
    # If Game ended then display the message and terminate
    if Hangman.wins >= 9:
        Hangman.end_theme()
        print("Congratulations! You've completed the game!")
        break

    # Level updates
    if (Hangman.wins==3 or Hangman.wins==6) and xflag==False:
        Hangman.levels+=1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("||<========CONGRATULATIONS! NEW LEVEL UNLOCKED=======>||")
        input('Press any key to continue: ')
        Hangman.print_guessed()
        xflag=True
    elif xflag==4 or xflag==7:
        xflag=False
    else:
        choice=input('Do you like to play Again(y/n): ')
        if choice.lower()=='n':
            break