
# Problem Set 2, hangman.py
# Name: mohamed hassan
# Time spent: 3 hours

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed=0
    for letter in secret_word:
        if letter in letters_guessed:
            guessed+=1
    if guessed==len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed=secret_word
    for letter in guessed :
        if letter not in letters_guessed :
            guessed=guessed.replace(letter, "_", secret_word.count(letter))
    return guessed



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters=string.ascii_lowercase
    for letter in letters_guessed:
        available_letters=available_letters.replace(letter,'')
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    counter=6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long."%len(secret_word))
    print("-------------")
    print("You have %d guesses left."%counter)
    print("Available letters:", string.ascii_lowercase)
    letters_guessed=[]
    warning=3
    vowels='eioau'
    while counter != 0:
        guess=str(input("Please guess a letter: "))
        if guess in string.ascii_lowercase:
            letters_guessed.append(guess)
            if guess in secret_word and guess !='':
                if is_word_guessed(secret_word,letters_guessed)==True:
                    break
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:",available_letters)
                print('-----------')
            elif guess not in secret_word and guess in vowels:
                counter-=2
                if counter<=0:
                    break
                print("That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:", available_letters)
                print('-----------')
            elif guess not in secret_word and guess not in vowels:
                counter-=1
                if counter<=0:
                    break
                print("That letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:", available_letters)
                print('-----------')
            elif guess in letters_guessed :
                if warning >= 0 :
                    warning-=1
                else :
                    counter-=1
                print("You've already guessed that letter.")
                print("You now have %d warnings :"%warning)
                print(get_guessed_word(secret_word, letters_guessed))
        else:
            if warning >= 0 :
                warning-=1
            else :
                counter-=1
            print("Oops! That is not a valid letter.")
            print("You have %d warnings left:"%warning, get_guessed_word(secret_word,letters_guessed))
            print("------------")
            print('You have %d guesses left.'%counter)
            available_letters=get_available_letters(letters_guessed)
            print("Available letters:", available_letters)
            print('-----------')
    if is_word_guessed(secret_word, letters_guessed)==True :
        score=counter*len(set(secret_word))
        print('Good guess:',get_guessed_word(secret_word,letters_guessed))
        print('------------')
        print('Congratulations, you won!')
        print('Your total score for this game is: %d'%score)
    else:
        print('Sorry, you ran out of guesses. The word was %s'%secret_word)



# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    alphabet=0 ; matches=0
    my_word=my_word.replace(' ', '', len(my_word))
    if len(my_word) != len(other_word):
        return False
    for letter in range(len(my_word)):
        if my_word[letter] in string.ascii_lowercase:
            alphabet+=1
            if my_word[letter]==other_word[letter]:
                matches+=1
    if alphabet == matches :
        return True




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches=0
    my_word=my_word.replace(' ','',len(my_word))
    for word in wordlist:
        if len(word) == len(my_word):
            isMatch = match_with_gaps((my_word), word)
            if isMatch == True:
                matches+=1
                print(word)
    if matches == 0:
        print('No matches found')




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    counter=6
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %d letters long."%len(secret_word))
    print("-------------")
    print("You have %d guesses left."%counter)
    print("Available letters:", string.ascii_lowercase)
    letters_guessed=[]
    warning=3
    vowels='eioau'
    while counter!=0 :
        guess=str(input("Please guess a letter: "))
        if guess in string.ascii_lowercase :
            letters_guessed.append(guess)
            if guess in secret_word and guess!='' :
                if is_word_guessed(secret_word, letters_guessed)==True :
                    break
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:", available_letters)
                print('-----------')
            elif guess not in secret_word and guess in vowels :
                counter-=2
                if counter <= 0 :
                    break
                print("That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:", available_letters)
                print('-----------')
            elif guess not in secret_word and guess not in vowels :
                counter-=1
                if counter <= 0 :
                    break
                print("That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                print("------------")
                print("You have %d guesses left."%counter)
                available_letters=get_available_letters(letters_guessed)
                print("Available letters:", available_letters)
                print('-----------')
            elif guess in letters_guessed :
                if warning >= 0 :
                    warning-=1
                else :
                    counter-=1
                print("You've already guessed that letter.")
                print("You now have %d warnings :"%warning)
                print(get_guessed_word(secret_word, letters_guessed))
        elif guess == '*':
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        else :
            if warning >= 0 :
                warning-=1
            else :
                counter-=1
            print("Oops! That is not a valid letter.")
            print("You have %d warnings left:"%warning, get_guessed_word(secret_word, letters_guessed))
            print("------------")
            print('You have %d guesses left.'%counter)
            available_letters=get_available_letters(letters_guessed)
            print("Available letters:", available_letters)
            print('-----------')
    if is_word_guessed(secret_word, letters_guessed)==True :
        score=counter*len(set(secret_word))
        print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        print('------------')
        print('Congratulations, you won!')
        print('Your total score for this game is: %d'%score)
    else :
        print('Sorry, you ran out of guesses. The word was %s'%secret_word)




if __name__ == "__main__":
    pass

    # uncomment the following lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    # To test hangman_with_hints re-comment the above lines and
    # uncomment the following lines.
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
