import time
import numpy as np
import pyautogui as pag

# set duration
low = 4 * 60
high = 4 * 60 + 30

while True:
    sleep_time = np.random.randint(low, high)
    print('Wait for', sleep_time, 'seconds before refreshing the page...')
    time.sleep(sleep_time)
    pag.press('f5')
