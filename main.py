import random

class WordChain:
    def __init__(self, words):
        self.words = words
        self.current_word = random.choice(self.words).lower()
        self.target_word = random.choice(self.words).lower()
        while self.target_word == self.current_word:
            self.target_word = random.choice(self.words).lower()
        self.guessed_words = set()
        self.max_attempts = 10
        self.attempts_left = self.max_attempts
    
    def play_game(self):
        print("Welcome to the Word Chain Game!")
        print(f"Find a chain of words from '{self.current_word}' to '{self.target_word}'.")
        print(f"You have {self.max_attempts} attempts.")
        
        while self.attempts_left > 0:
            print(f"\nCurrent word: {self.current_word}")
            print(f"Remaining attempts: {self.attempts_left}")
            
            guess = input("Enter your word guess: ").strip().lower()
            
            if guess not in self.words:
                print("Invalid word! Please enter a valid English word.")
                continue
            
            if guess in self.guessed_words:
                print("You've already guessed that word!")
                continue
            
            if self.is_valid_step(self.current_word, guess):
                self.current_word = guess
                self.guessed_words.add(guess)
                
                if self.current_word == self.target_word:
                    print(f"Congratulations! You've reached the target word '{self.target_word}'.")
                    break
            else:
                print("Sorry, that word doesn't form a valid chain from the current word.")
            
            self.attempts_left -= 1
        
        if self.attempts_left == 0:
            print(f"\nGame over! You've run out of attempts. The target word was '{self.target_word}'.")
    
    def is_valid_step(self, current_word, guess_word):
        if len(current_word) != len(guess_word):
            return False
        diff_count = sum(1 for c1, c2 in zip(current_word, guess_word) if c1 != c2)
        return diff_count == 1

if __name__ == "__main__":
    # Example usage with a list of words
    words = ['cat', 'bat', 'hat', 'heat', 'beat', 'bead', 'bed', 'bad']
    game = WordChain(words)
    game.play_game()
