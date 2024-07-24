from pathlib import Path
import os
import re
from pynput.keyboard import Key, Controller
import time
import random
import math
import win32api, win32con, pywintypes
import traceback
import configparser
from tkinter import *

keyboard = Controller()
def results():
	while True:
		paths = 0
		try:
			paths = sorted(Path("E:\WarThunder\Screenshots").iterdir(), key=os.path.getmtime)
		except FileNotFoundError:
			paths = sorted(Path("E:\WarThunder\Screenshots").iterdir(), key=os.path.getmtime)
		screenshot_name = ''
		if len(paths) > 0:
			screenshot = open(paths[len(paths)-1], 'rb')
			screenshot_name = screenshot.name
			screenshot.close()
		keyboard.press(Key.print_screen) 
		time.sleep(random.uniform(0.05, 0.15))
		keyboard.release(Key.print_screen)
		retries = 0
		while retries < 25:
			try:
				paths = sorted(Path("E:\WarThunder\Screenshots").iterdir(), key=os.path.getmtime)
			except FileNotFoundError:
				paths = sorted(Path("E:\WarThunder\Screenshots").iterdir(), key=os.path.getmtime)
			if len(paths) > 0:
				screenshot = open(paths[len(paths)-1], 'rb')
				if screenshot_name != screenshot.name:
					break
				screenshot.close()    
			time.sleep(0.15)
			retries += 1
		if retries == 25:
			continue
		time.sleep(0.3)
		data = screenshot.read()
		screenshot.close()
		direction = re.search(r'dir:p3=(.+?)\\' , str(data))
		direction = direction[1].split(', ')
		x1 = float(direction[0])
		y1 = float(direction[1])
		z1 = float(direction[2])
		azimuth = math.degrees(2*math.pi + psi) if (psi := math.atan2(x1, z1)) < 0.0 else math.degrees(psi)
		elevation = math.degrees(math.atan(y1/math.hypot(x1, z1)))
		print(elevation, azimuth)
		text1 = f'Угол: {elevation} \n Азимут: {azimuth}'
		os.remove(paths[len(paths)-1])
		label.config(text = text1)
		break
root = Tk()
root.geometry('+1080+540')
root.overrideredirect(True) 
root.configure(bg='white')
root.wm_attributes('-topmost', 1)  
root.attributes("-transparentcolor", 'white')

label = Label(root, text="", font=("Arial", 12), bg='white', fg='yellow')
label.pack(padx=10, pady=10)


while True:
  results()
  root.update()


root.mainloop()

	
	



