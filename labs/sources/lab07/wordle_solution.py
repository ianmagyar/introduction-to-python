import random


def load_words(dataset_path):
    words = list()
    try:
        with open(dataset_path, 'r') as dset_file:
            lines = dset_file.readlines()

        for line in lines:
            word = line[:-1]
            if len(word) == 5:
                words.append(word)
    except FileNotFoundError:
        return list()

    return words


def get_puzzle(word_list):
    return random.choice(word_list)


def is_game_finished(guess, puzzle):
    return guess.lower() == puzzle.lower()


def evaluate_guess(guess, puzzle):
    guess = guess.lower()
    puzzle = puzzle.lower()

    evaluation = list()

    for idx, letter in enumerate(guess):
        contains = letter in puzzle
        right_position = letter == puzzle[idx]
        evaluation.append((letter, contains, right_position))

    return evaluation


def start_game(dataset_path):
    # nepovinne - iba pre testovanie
    word_list = load_words(dataset_path)
    puzzle = get_puzzle(word_list)

    for _ in range(6):
        guess = input("Enter your guess: ")
        while guess not in word_list:
            print("Sorry, I did not find that word!")
            guess = input("Enter your guess: ")

        result = evaluate_guess(guess, puzzle)
        print(result)

        if is_game_finished(guess, puzzle):
            print("You win!")
            return
    else:
        print("You ran out of attempts. The word I was looking for was", puzzle)
        return


if __name__ == '__main__':
    start_game("word_list.txt")
