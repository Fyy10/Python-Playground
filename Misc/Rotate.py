import pyautogui as pag
import math

# get screen size
width, height = pag.size()
print(width, height)

# radius
r = 0.25 * min(width, height)

# center
o_x = width/2
o_y = height/2

pi = math.acos(-1)

ans = pag.confirm('The cursor is going to rotate, confirm? You can stop rotating by moving your cursor to the upper-left corner of the screen.')

# rotate n times
n = 10 if ans == 'OK' else 0

# rotate
for i in range(n):
    for angle in range(0, 360, 1):
        X = o_x + r * math.cos(-8 * angle * pi / 180)
        Y = o_y + r * math.sin(-9 * angle * pi / 180)

        pag.moveTo(X, Y, duration=0)
