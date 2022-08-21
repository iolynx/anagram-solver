import itertools
import time
import pyautogui as pg
import keyboard
import enchant
import clipboard

d = enchant.Dict('en-US')
while True:
    if keyboard.is_pressed('enter'):
        letters = clipboard.paste()
        break
print("reached 1")
final_list = []
letters = letters.replace(" ", "")
letters = letters.lower()
print(letters)

p = []
for i in range(3, 8):
    p.append(itertools.permutations(letters, i))
    
print("reached")

for k in range(len(p)):
    for i in list(p[k]):
        if d.check(''.join(i)) and ''.join(i) not in final_list:
            final_list.append(''.join(i))
print(final_list)
print("reached final")
'''
for i in reversed(final_list):
    pg.write((i), interval = 0.15)
    pg.press('enter')
'''

for i in reversed(final_list):
    print(i)