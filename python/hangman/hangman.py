# Game status categories
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word:str):
        self.word = word
        self.hits = set(word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char:str):
        """ Core logic of the game. """
        # Check status of the game
        if self.status != STATUS_ONGOING:
            raise ValueError('Game is over.')
        
        # It is a first time hit -> OK
        if char in self.word and char in self.hits:
            self.hits.remove(char)
        # It was previously guessed as hit or miss -> Penalty
        else:
            self.remaining_guesses -= 1
        
        # Update status of the game
        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        elif not self.hits:
            self.status = STATUS_WIN

    def get_masked_word(self):
        """ Returns a masked version of the word to guess. """
        return ''.join('_' if c in self.hits else c for c in self.word)

    def get_status(self):
        """ Returns the status of the game. """
        return self.status
