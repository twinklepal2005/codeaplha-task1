import random

# Dictionary with words as keys and hints as values
words_with_hints = {
    'python': 'A popular programming language named after a snake.',
    'java': 'A high-level programming language originally developed by Sun Microsystems.',
    'javascript': 'A programming language commonly used in web development.',
    'php': 'A server-side scripting language often used for web development.',
    'ruby': 'A dynamic, open-source programming language with a focus on simplicity.',
    'csharp': 'A programming language developed by Microsoft.',
    'swift': 'A programming language created by Apple for iOS and macOS development.',
    'kotlin': 'A modern programming language used primarily for Android development.'
}

word, hint = random.choice(list(words_with_hints.items()))

hidden_word = ['_'] * len(word)
attempts_left = 7
incorrect_guesses = 0

def print_hangman(chances):
    if chances == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif chances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif chances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|             ")
        print("|             ")
    elif chances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|     /       ")
        print("|             ")
    elif chances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\\     ")
        print("|     / \\     ")
        print("|             ")

a=input("Enter your name:")
print("\nWELCOME",a,"TO THE HANGMAN GAME!!!!")
print("\nGameplay:")
print("The game starts with a random word selection from a predefined dictionary.")
print("The player is presented with a hint related to the word.")
print("The player goal is to guess the word by suggesting letters.")
print("For each letter guessed, the game checks if the letter appears in the word.")
print("If the letter appears in the word, the game fills in the corresponding blanks.")
print("If the letter does not appear in the word, the game draws a part of a hangmans gallows.")
print("The player has a limited number of attempts (7) to guess the word.")
print("If the player guesses the word correctly before running out of attempts, they win.")
print("If the player runs out of attempts before guessing the word, they lose.")


print(f"\nHint: {hint}")

while '_' in hidden_word and incorrect_guesses < attempts_left:
    guess = input('Guess a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        incorrect_guesses += 1
        print_hangman(attempts_left - incorrect_guesses)
        print(f'Incorrect guess. You have {attempts_left - incorrect_guesses} more attempts.')

    print(' '.join(hidden_word))

    if '_' not in hidden_word:
        print('Congratulations! You guessed the word.')
        break
    elif incorrect_guesses >= attempts_left:
        print(f'Sorry, you lost. The word was {word}')
        break
