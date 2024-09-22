import cv2
import pyautogui
import time
from pynput import keyboard  # Import pynput for keyboard event handling

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

# Global flag to stop the loop
running = True

# Define a callback function to stop the program when 'q' is pressed
def on_press(key):
    global running
    try:
        if key.char == 'q':  # Exit when 'q' is pressed
            running = False
            return False  # Stop the listener
    except AttributeError:
        pass

# Set up the listener in a non-blocking way
listener = keyboard.Listener(on_press=on_press)
listener.start()

while running:
    # Take a screenshot of the game window
    pyautogui.screenshot("/home/tacodi/python opencv/whackabot/image.png", region=(x, y, w, h))
    image = cv2.imread("/home/tacodi/python opencv/whackabot/image.png")
    
    if image is None:
        print("Error: Screenshot could not be loaded.")
        continue

    # Convert the screenshot to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Match the template in the screenshot
    result = cv2.matchTemplate(image_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"Max Value: {max_val}, Max Location: {max_loc}")  # Debug info

    # Display what the bot "sees"
    image_mini = cv2.resize(image, (720, 420))
    cv2.imshow("Vision Window", image_mini)
    
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

    else:
        print("No match found above the threshold")

    # Press 'Esc' to exit the OpenCV window (optional)
    if cv2.waitKey(1) == 27:  # Escape key to exit OpenCV window
        break

# Clean up windows
cv2.destroyAllWindows()

# Stop the listener after the loop ends
listener.stop()
