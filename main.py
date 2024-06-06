from random import choice


def initialize_word_list():
    with open("CROSSWD.TXT") as wd_file:
        wd_list = wd_file.read().splitlines()
    return [wd for wd in wd_list if len(wd) == 5]


class WordleSolver:

    def __init__(self):
        self.words = initialize_word_list()
        self.guesses = []
        self.results = []
        self.word_found = False

        while not self.word_found:
            self.guess()

        print("Congratulations, you found the word in {} guesses!".format(len(self.guesses)))

    def guess(self):
        self.guesses.append(choice(self.words))
        print("Word to guess is: {}".format(self.guesses[-1]))
        while True:
            result = input("Input results with G for Green, Y for Yellow, and B for Blank: ")
            if len(result) == 5 and all([x in 'GYB' for x in result]):
                break
            else:
                print("Incorrect format. Please input results with G for Green, Y for Yellow, and B for Blank")

        self.results.append(result)
        if result == "GGGGG":
            self.word_found = True
        else:
            for i in range(5):
                guess = self.guesses[-1]
                letter = guess[i]
                if result[i] == "G":
                    self.words = [wd for wd in self.words if wd[i] == letter]
                elif result[i] == "Y":
                    self.words = [wd for wd in self.words if letter in wd and wd[i] != letter]
                else:
                    if not any([result[i] == "G" and guess[i] == letter for i in range(5)]):
                        self.words = [wd for wd in self.words if letter not in wd]					
		

if __name__ == '__main__':
    WordleSolver()
