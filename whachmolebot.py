# https://www.classicgame.com/game/Whack+a+Mole

import cv2
import pyautogui
import time
import numpy as np

# No cooldown time
pyautogui.PAUSE = 0

# Load the template image
template = cv2.imread('/home/tacodi/python opencv/whackabot/noiseimg.png')

# Check if the template was loaded successfully
if template is None:
    print("Error: Template image not found or couldn't be loaded.")
    exit()

# Convert the template to grayscale
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template_w, template_h = template_gray.shape[::-1]

# Game window dimensions
x, y, w, h = 400, 325, 1031, 977

# Wait for the game to start
time.sleep(5)

while True:
    # Take a screenshot of the game window
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV
    
    if image is None:
        print("Error: Screenshot could not be loaded.")
        continue

    # Convert the screenshot to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Match the template in the screenshot
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"Max Value: {max_val}, Max Location: {max_loc}")  # Debug info

    # Threshold for matching
    if max_val >= 0.8:
        # Calculate screen coordinates for the click
        click_x = max_loc[0] + x
        click_y = max_loc[1] + y
        
        # Click the matched location
        pyautogui.click(x=click_x, y=click_y)
        print(f"Click at: {click_x}, {click_y}")

        # Draw a rectangle around the detected area
        image = cv2.rectangle(image, max_loc, (max_loc[0] + template_w, max_loc[1] + template_h), (0, 0, 255), 2)
    
    # Display what the bot "sees"
    cv2.imshow("Vision Window", image)

    # Wait for 'q' key press to exit the loop
    key = cv2.waitKey(1)  # 1 millisecond wait for real-time response
    if key == ord('q'):  # Press 'q' to quit
        break

# Clean up windows
cv2.destroyAllWindows()
