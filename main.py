import pyautogui as pag
import random
import time

curr_coords = pag.position()  # records initial position of the cursor
afk_counter = 0  # how long you've been afk

while True:
    if (
        pag.position() == curr_coords
    ):  # if the mouse has not moved, it adds 1 to the afk counter
        afk_counter += 1
    else:
        afk_counter = 0
        curr_coords = (
            pag.position()
        )  # if the mouse has moved, afk counter is set back to 0
    if afk_counter > 5:  # if you've been afk for 5 seconds, it will move the cursor
        x = random.randint(2560, 5120)
        y = random.randint(1, 1440)
        pag.moveTo(x, y, 0.5)
        curr_coords = pag.position()
    print(f"AFK Counter: {afk_counter}")
    time.sleep(2)
