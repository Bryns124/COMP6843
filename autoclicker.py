import pyautogui
import time

click_x, click_y = 629, 643
start_x, start_y = pyautogui.position()
movement_threshold = 20
time.sleep(2)

while True:
    pyautogui.click(x=click_x, y=click_y)
    current_x, current_y = pyautogui.position()
    distance_moved = ((current_x - start_x) ** 2 + (current_y - start_y) ** 2) ** 0.5
    if distance_moved > movement_threshold:
        print("Mouse moved from start position, stopping script.")
        break
print("Script completed or stopped due to mouse movement.")
