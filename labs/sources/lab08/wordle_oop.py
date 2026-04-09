from copy import deepcopy
import random
import string


PLAYER_KNOWLEDGE = [(letter, None, -1)
                    for letter in string.ascii_lowercase]


class Puzzle:
    def __init__(self, word):
        self.puzzle = word.lower()

    def is_game_finished(self, guess):
        return False

    def evaluate_guess(self, guess):
        return list()


class Game:
    def __init__(self, dataset_path):
        self.word_list = self.load_words(dataset_path)
        self.puzzle = None

    def load_words(self, dataset_path):
        return list()

    def generate_puzzle(self):
        pass

    def start_game(self):
        pass

    def bot_game(self, bot):
        pass


class Bot:
    def __init__(self, word_list):
        self.reset(word_list)

    def reset(self, word_list):
        pass

    def get_player_guess(self):
        return ""

    def process_result(self, result):
        pass


if __name__ == '__main__':
    wordle = Game("word_list.txt")
    wordle.start_game()
