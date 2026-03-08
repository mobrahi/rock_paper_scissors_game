# 🪨📄✂️ Rock, Paper, Scissors Game

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)

A feature-rich **Rock, Paper, Scissors** game built with Python. Play against the computer in this classic hand game with modern features and fun emojis!

![Gameplay Screenshot](https://via.placeholder.com/800x400?text=Rock+Paper+Scissors+Gameplay)

## ✨ Features

### Core Gameplay
- **Full Match Mode** - Best of 5 rounds
- **Quick Play Mode** - Single round for fast games
- **Score Tracking** - Keep track of wins
- **Round History** - See all rounds played

### Interactive Elements
- **Emoji Interface** - Fun visual representation
- **Personalized Experience** - Enter your name
- **Dramatic Pauses** - Built-in delays for tension
- **Statistics** - Win rates and performance metrics

### Game Modes
| Mode | Description | Best For |
|------|-------------|----------|
| 🎮 **Full Match** | First to 3 wins | Serious competition |
| ⚡ **Quick Play** | Single round | Quick breaks |

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed

### Installation & Play

```bash
# Clone the repository
git clone https://github.com/yourusername/rock-paper-scissors.git

# Navigate to project
cd rock-paper-scissors

# Run the game
python rock_paper_scissors.py
```

## 🎯 How to Play

### Game Rules
```
📋 RULES:
• Rock 🪨 beats Scissors ✂️
• Paper 📄 beats Rock 🪨
• Scissors ✂️ beats Paper 📄
• First to 3 wins takes the match!
```

### Sample Gameplay
```
============================================================
🎮 Welcome to ROCK, PAPER, SCISSORS!
============================================================

What's your name? Alex
Nice to meet you, Alex! Let's play! 🎉

============================================================
ROUND 1
============================================================

Alex's turn...
Your choice (rock/paper/scissors): rock
💻 Computer chose: 📄 Paper

----------------------------------------
Alex: 🪨 rock
Computer: 📄 paper
----------------------------------------
💻 Computer wins this round!

📊 SCORE: Alex 0 - 1 Computer

============================================================
ROUND 2
============================================================

Alex's turn...
Your choice (rock/paper/scissors): scissors
💻 Computer chose: ✂️ scissors

----------------------------------------
Alex: ✂️ scissors
Computer: ✂️ scissors
----------------------------------------
🤝 It's a tie!

📊 SCORE: Alex 0 - 1 Computer
```

### 📊 Game Statistics

After each match, you'll see detailed statistics:
```
📊 MATCH STATISTICS
========================================
Total rounds played: 5
Alex wins: 3 (60.0%)
Computer wins: 1 (20.0%)
Ties: 1 (20.0%)
```

## 🛠️ Code Structure

```
class RockPaperScissors:
    ├── __init__()           # Game setup
    ├── get_player_name()    # Personalization
    ├── display_rules()      # Show rules
    ├── get_player_choice()  # Input handling
    ├── get_computer_choice() # AI choice
    ├── determine_winner()   # Game logic
    ├── play_round()         # Single round
    ├── check_match_winner() # Match completion
    └── show_stats()         # Display results
```
    
## 🚀 Possible Enhancements
```
Sound Effects - Add win/lose sounds
GUI Version - Using tkinter or pygame
Multiplayer - Two-player mode
Difficulty Levels - Computer strategy changes
Leaderboard - Save high scores
Animations - ASCII art animations
Best of 7/9 - More match options
Custom Names - Name the computer
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
```
🐛 Report bugs
💡 Suggest features
🔧 Submit pull requests
```

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

Mohd Fairuz

GitHub: @mobrahi
Twitter: @faairuz

## ⭐ Show Your Support

Give a ⭐ if this project helped you learn!

Made with ❤️ for Python beginners