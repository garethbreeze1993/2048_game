from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import action_chains
from selenium.webdriver.support.ui import WebDriverWait
import random
import time

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('body')
actions = action_chains.ActionChains(browser)

browser.find_element_by_class_name('grid-container').click()
keys_tuple = (Keys.UP,Keys.RIGHT,Keys.DOWN,Keys.LEFT)

def prompt():
	prompt = input('Would you like to play again Y or N? ')
	if prompt == 'Y':
		retryElem = browser.find_element_by_class_name('retry-button')
		retryElem.click()
		game()

def game():
	x = True
	y = False
	while x == True:	
	
		try:
			browserElem = browser.find_element_by_class_name('game-over')
		#WebDriverWait(browser, .00001).until(
		#EC.presence_of_element_located((By.ID, "game-message game-over")))
			print('try')
			x = False
			y = True
		
		

	
		except:
			time.sleep(3)
	

		if y == True:
			browserElem.click()
			print('Hello')
			prompt()
		
		else:	
			actions.send_keys(keys_tuple).perform()

game()
print('Game finished')

	
print('Thankyou for playing')	
