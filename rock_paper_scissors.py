# rock_paper_scissors.py
import random
import time

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.emoji_map = {
            'rock': '🪨',
            'paper': '📄',
            'scissors': '✂️'
        }
        self.win_map = {
            'rock': 'scissors',
            'paper': 'rock',
            'scissors': 'paper'
        }
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.player_name = ""
    
    def get_player_name(self):
        print("\n" + "="*60)
        print("🎮 Welcome to ROCK, PAPER, SCISSORS!")
        print("="*60)
        self.player_name = input("\nWhat's your name? ").strip()
        if not self.player_name:
            self.player_name = "Player"
        print(f"Nice to meet you, {self.player_name}! Let's play! 🎉")
    
    def display_rules(self):
        print("\n📋 RULES:")
        print("• Rock 🪨 beats Scissors ✂️")
        print("• Paper 📄 beats Rock 🪨")
        print("• Scissors ✂️ beats Paper 📄")
        print("• First to 3 wins takes the match!")
        print("\nCommands: 'rock', 'paper', 'scissors' or 'quit' to exit")
    
    def get_player_choice(self):
        while True:
            print(f"\n{self.player_name}'s turn...")
            choice = input("Your choice (rock/paper/scissors): ").strip().lower()
            
            if choice == 'quit':
                return 'quit'
            
            if choice in self.choices:
                return choice
            
            print("❌ Invalid choice! Please enter rock, paper, or scissors.")
    
    def get_computer_choice(self):
        choice = random.choice(self.choices)
        print(f"💻 Computer chose: {self.emoji_map[choice]} {choice.capitalize()}")
        return choice
    
    def determine_winner(self, player, computer):
        if player == computer:
            return 'tie'
        elif self.win_map[player] == computer:
            return 'player'
        else:
            return 'computer'
    
    def display_round_result(self, winner, player_choice, computer_choice):
        print("\n" + "-"*40)
        print(f"{self.player_name}: {self.emoji_map[player_choice]} {player_choice.capitalize()}")
        print(f"Computer: {self.emoji_map[computer_choice]} {computer_choice.capitalize()}")
        print("-"*40)
        
        if winner == 'player':
            print(f"🎉 {self.player_name} wins this round!")
            self.player_score += 1
        elif winner == 'computer':
            print("💻 Computer wins this round!")
            self.computer_score += 1
        else:
            print("🤝 It's a tie!")
        
        print(f"\n📊 SCORE: {self.player_name} {self.player_score} - {self.computer_score} Computer")
    
    def play_round(self):
        print(f"\n{'='*60}")
        print(f"ROUND {self.rounds_played + 1}")
        print(f"{'='*60}")
        
        player_choice = self.get_player_choice()
        if player_choice == 'quit':
            return False
        
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(player_choice, computer_choice)
        self.display_round_result(winner, player_choice, computer_choice)
        
        self.rounds_played += 1
        time.sleep(1.5)
        return True
    
    def check_match_winner(self):
        if self.player_score >= 3:
            print("\n" + "="*50)
            print(f"🏆 CHAMPION! {self.player_name} WINS THE MATCH! 🏆")
            print("="*50)
            return True
        elif self.computer_score >= 3:
            print("\n" + "="*50)
            print("💻 COMPUTER WINS THE MATCH! Better luck next time! 💻")
            print("="*50)
            return True
        return False
    
    def play_again(self):
        print("\n" + "-"*40)
        choice = input("Would you like to play another match? (yes/no): ").strip().lower()
        return choice == 'yes'
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
    
    def show_stats(self):
        total_rounds = self.rounds_played
        if total_rounds > 0:
            player_win_rate = (self.player_score / total_rounds) * 100
            computer_win_rate = (self.computer_score / total_rounds) * 100
            ties = total_rounds - self.player_score - self.computer_score
            tie_rate = (ties / total_rounds) * 100
            
            print("\n📊 MATCH STATISTICS")
            print("="*40)
            print(f"Total rounds played: {total_rounds}")
            print(f"{self.player_name} wins: {self.player_score} ({player_win_rate:.1f}%)")
            print(f"Computer wins: {self.computer_score} ({computer_win_rate:.1f}%)")
            print(f"Ties: {ties} ({tie_rate:.1f}%)")
    
    def run(self):
        self.get_player_name()
        
        while True:
            self.display_rules()
            self.reset_game()
            
            while self.player_score < 3 and self.computer_score < 3:
                if not self.play_round():
                    print("\n👋 Thanks for playing! Come back soon!")
                    return
            
            self.show_stats()
            
            if not self.play_again():
                print("\n👋 Thanks for playing! See you next time!")
                break
            else:
                print("\n🔄 Starting new match...")
                time.sleep(1)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()