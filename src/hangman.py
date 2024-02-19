import os

class Hangman:
    
    total_games = 0
    wins = 0
    levels=1
    def __init__(self, secret_word, max_guesses):
        """
        Declare and Initialize object variables
        """
        self.letters_guessed = []
        self.mistakes_made = 0
        self.secret_word=secret_word
        self.mx_guess=max_guesses
        self.guess_count=0
      
    
    def play(self):
        """
        Actually play the hangman game
        """
               
        self.mistakes_made=0
        while self.mistakes_made < self.mx_guess:
            guessed_letter=input('Enter Guess: ')

            if len(guessed_letter) != 1: # Invalid exception handler
                print("Please enter only a single character.")
                continue
            if guessed_letter not in self.letters_guessed:
                self.letters_guessed.append(guessed_letter)
            if guessed_letter not in self.secret_word:
                self.mistakes_made+=1
            elif guessed_letter in self.secret_word:
                self.guess_count+=1

            self.print_guessed()
            # If the word is Guessed
            if self.word_guessed():
                Hangman.wins+=1
                Hangman.total_games+=1
                print('Game Won!')
                break
        
        if self.word_guessed() == False:
            Hangman.total_games+=1
            print('Game lost. You ran out of guesses!')
        


            


    def word_guessed(self):
        """
        Returns True if the player has successfully guessed the word,
        and False otherwise.
        """

        return all(letter in self.letters_guessed for letter in self.secret_word)


    def print_guessed(self):
        """
        Prints out the dashes and characters you have guessed in the
        secret word so far.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("<<=============WELCOME TO HANGMAN==================>>")
        print(f"Lets Hang::---------(|LEVEL-{Hangman.levels}|)")
        print()
        print(f"\nThe word has {len((self.secret_word))} characters.")
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                print(letter, end='')
            else:
                print('-', end='')

        print('                        ', end='')
        for i in range(self.mistakes_made):
            print('|', end='')
        print()

    def end_theme():
        print("""
        _   _                 _                                     
        | | | |               | |                                    
        | |_| | ___  __ _  ___| | __   ___  _ __   ___ _ __ ___   ___ 
        |  _  |/ _ \/ _` |/ __| |/ /  / _ \| '_ \ / _ \ '_ ` _ \ / _ \\
        | | | |  __/ (_| | (__|   <  | (_) | | | |  __/ | | | | |  __/
        \_| |_/\___|\__,_|\___|_|\_\  \___/|_| |_|\___|_| |_| |_|\___|                                                          
            """)