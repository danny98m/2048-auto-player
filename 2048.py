#! /usr/bin/env python3

"""
This program uses selenium to 
continuously make the moves up
up, right, down, then left
on a game of 2048.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()
driver.get('https://gabrielecirulli.github.io/2048/')

htmlElem = driver.find_element_by_tag_name('html')
while True:
	htmlElem.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)

	try:
		stopElem = driver.find_element_by_class_name('game-over')
		break
	except:
		continue
