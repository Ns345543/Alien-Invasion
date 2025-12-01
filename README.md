![Screenshot](https://github.com/user-attachments/assets/cbc907a6-d4c4-45dd-a22e-02ac21974a04)

# 🚀 Alien Invasion Game

A classic space shooter game built with Python and Pygame. Defend Earth from waves of alien invaders in this action-packed arcade-style game!

## 📖 Table of Contents

- [About the Game](#-about-the-game)
- [Features](#-features)
- [Installation](#-installation)
- [How to Play](#-how-to-play)
- [Keyboard Shortcuts](#️-keyboard-shortcuts)
- [Game Mechanics](#-game-mechanics)
- [Project Structure](#-project-structure)
- [Building Executable](#-building-executable)
- [Requirements](#-requirements)
- [Credits](#-credits)

## 🎮 About the Game

Alien Invasion is a classic arcade-style space shooter game where you control a spaceship at the bottom of the screen and must defend against waves of descending alien invaders. The game features progressive difficulty, scoring system, high score tracking, and sound effects for an immersive gaming experience.

## ✨ Features

- **Progressive Difficulty**: Game speed and alien points increase with each level
- **Scoring System**: Earn points by destroying aliens, with increasing rewards at higher levels
- **High Score Tracking**: Your best score is saved and displayed
- **Lives System**: Start with 3 lives - lose one when hit by aliens or when they reach the bottom
- **Sound Effects**: Immersive audio for bullets and game events
- **Fullscreen Mode**: Toggle between windowed and fullscreen display
- **Resizable Window**: Dynamically adjust window size with responsive UI elements
- **Level Progression**: Advance through increasingly challenging levels
- **Visual Polish**: Custom graphics for ships, aliens, and starry space background

## 🔧 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or Download the Repository**
   ```bash
   git clone https://github.com/Ns345543/Alien-Invasion.git
   cd Alien-Invasion
   ```

2. **Create a Virtual Environment** (Recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Required Packages**
   ```bash
   pip install pygame
   ```

5. **Run the Game**
   ```bash
   cd "AlienInvasion Game"
   python Alien_invasion.py
   ```

## 🎯 How to Play

1. **Starting the Game**: Click the "Play" button or press any key when the game starts
2. **Movement**: Use arrow keys or WASD to move your ship left and right
3. **Shooting**: Press SPACEBAR to fire bullets at the aliens
4. **Objective**: Destroy all aliens to advance to the next level
5. **Survival**: Avoid letting aliens reach the bottom or collide with your ship
6. **Game Over**: The game ends when you lose all 3 lives

### Scoring

- Each alien destroyed earns you points
- Points increase progressively with each level (multiplied by 1.5x)
- Starting value: **50 points** per alien
- Try to beat your high score!

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **Arrow Keys** or **A/D** | Move ship left/right |
| **LEFT ARROW** or **A** | Move ship left |
| **RIGHT ARROW** or **D** | Move ship right |
| **SPACEBAR** | Fire bullets |
| **F11** | Toggle fullscreen mode |
| **Q** | Quit game |
| **Mouse Click** | Click "Play" button to start/restart |

## 🎲 Game Mechanics

### Difficulty Progression

- **Speed Increase**: Ship, bullets, and aliens move 1.2x faster each level
- **Score Multiplier**: Alien points increase by 1.5x each level
- **Fleet Behavior**: Aliens move horizontally and drop down when reaching screen edges

### Lives and Game Over

- You start with **3 lives** (displayed as ship icons in the top-left corner)
- Lose a life when:
  - An alien collides with your ship
  - Aliens reach the bottom of the screen
- Game over when all lives are lost
- Level resets to 1 after game over

### Bullet System

- Maximum of **4 bullets** on screen at once
- Bullets are removed when they hit aliens or reach the top of the screen
- Bullet firing produces a sound effect

## 📁 Project Structure

```
Alien Invasion/
├── AlienInvasion Game/
│   ├── Alien_invasion.py      # Main game file
│   ├── alien.py                # Alien sprite class
│   ├── bullet.py               # Bullet sprite class
│   ├── button.py               # Play button UI element
│   ├── game_stats.py           # Game statistics tracker
│   ├── scoreboard.py           # Score display and UI
│   ├── settings.py             # Game configuration settings
│   ├── ship.py                 # Player ship class
│   ├── soundManager.py         # Sound effects manager
│   ├── path_utils.py           # Path utility functions
│   ├── build_exe.py            # PyInstaller build script
│   ├── build_game.py           # Alternative build script
│   ├── build.bat               # Windows build batch file
│   ├── Alien_invasion.spec     # PyInstaller specification
│   ├── images/                 # Game graphics
│   │   ├── AlienInvasion.logo.png
│   │   ├── Ship.png
│   │   ├── alienShip.png
│   │   ├── bg_space.jpg
│   │   ├── playerShip2_orange.png
│   │   └── star-image.png
│   └── Sfx/                    # Sound effects
│       └── lowRandom.ogg
├── .venv/                      # Virtual environment (if created)
├── .git/                       # Git repository
└── README.md                   # This file
```

## 🔨 Building Executable

To create a standalone executable (.exe) file:

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable**
   ```bash
   python build_exe.py
   ```
   Or use the batch file (Windows only):
   ```bash
   build.bat
   ```

3. **Locate the Executable**
   - The `.exe` file will be in the `dist/Alien_invasion/` folder
   - You can distribute this folder to run the game without Python installed

## 📦 Requirements

- **Python**: 3.7+
- **Pygame**: Latest version
- **PyInstaller**: For building executables (optional)

### Installing Requirements

```bash
pip install pygame
```

For building executables:
```bash
pip install pyinstaller
```

## 🎨 Credits

**Developer**: Nitin  
**Framework**: Pygame  
**Inspired by**: Classic arcade space shooter games

### Assets

- Custom graphics for ships and aliens
- Space-themed background
- Sound effects for enhanced gameplay

---

## 🐛 Troubleshooting

### Game Won't Start
- Ensure Python 3.7+ is installed
- Verify pygame is installed: `pip install pygame`
- Check that you're in the correct directory

### No Sound
- Ensure sound files are in the `Sfx/` folder
- Check system audio settings
- Verify pygame mixer is working

### Executable Errors
- Ensure all asset folders (`images/`, `Sfx/`) are included in the build
- Use the provided `.spec` file for PyInstaller
- Check that `path_utils.py` correctly handles frozen app paths

---

## 🚀 Future Enhancements

- [ ] Power-ups and special weapons
- [ ] Multiple alien types with different behaviors
- [ ] Boss battles
- [ ] Local multiplayer mode
- [ ] Additional sound effects and background music
- [ ] Game settings menu
- [ ] Difficulty selection

---

**Enjoy the game and may the best score win! 🌟**
