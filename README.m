

# Whack-a-Mole Bot

## Overview
The Whack-a-Mole bot is an automated script developed using Python, OpenCV, and PyAutoGUI to play the classic Whack-a-Mole game. The bot detects moles appearing on the screen and clicks on them in real-time, aiming to maximize the score.

## Features
- Real-time detection of moles using template matching.
- Automated mouse clicks on detected moles.
- Simple user interface for monitoring the game state.
- Option to stop the bot by pressing the 'q' key.

## Requirements
- Python 3.x
- OpenCV
- PyAutoGUI
- NumPy
- PIL (Pillow)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/whack-a-mole-bot.git
   cd whack-a-mole-bot
   ```

2. **Install the required packages:**
   ```bash
   pip install opencv-python pyautogui numpy pillow
   ```

3. **Set up the template image:**
   - Place your template image (e.g., `noiseimg.png`) in the `whackabot` folder.

## Usage
1. Open the Whack-a-Mole game in a windowed mode.
2. Adjust the `game window dimensions` in the script to match your game’s position and size.
3. Run the bot:
   ```bash
   python whachamolegamebot.py
   ```
4. The bot will start after a 5-second delay, allowing you to prepare.
5. Press the 'q' key at any time to stop the bot.

## Code Structure
- **whachamolegamebot.py**: Main script for the bot functionality.
- **noiseimg.png**: Template image used for detecting moles.

## Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.



## Acknowledgments
- OpenCV for image processing.
- PyAutoGUI for simulating mouse clicks.
- Inspiration from the classic Whack-a-Mole game.


