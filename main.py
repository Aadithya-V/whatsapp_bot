import pyautogui as pt 
from time import sleep 
import pyperclip
import random 


sleep(3)  


position1 = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence = .6)         # confidence is the acceptable look alikeness of the picture
x = position1[0]
y = position1[1]

# function to copy onscreen text to a variable

def copy_to_variable():
    pt.hotkey('ctrl','c')
    sleep(0.1)
    copied_msg = pyperclip.paste()
    return(copied_msg)

# Getting recieved message

def get_message():
    pt.moveTo(x, y, duration = .01)
    pt.moveTo(x + 86, y - 40, duration = .01)
    sleep(.01)
    pt.tripleClick()
    sleep(.01)
   
    whatsapp_message = copy_to_variable()
    return whatsapp_message


#Sending response (as of now the got message) 

def post_response(message) :
    pt.moveTo(x + 150, y + 25, duration = .01)   
    pt.click()
    sleep(.1)
    pt.write(message + "\n", interval=.001)         #\n is interpreted as enter to newline character and sends the message


# Processing the response

#def process_response(message) :






post_response(get_message())
