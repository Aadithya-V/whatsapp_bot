import pyautogui as pt 
from time import sleep 
import pyperclip
import random 

sleep(5) #add a voice "the bot is now functional"


position1 = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence = .6)         # confidence is the acceptable look alikeness of the picture
x = position1[0]
y = position1[1]

# Gets message

def get_message():
    pt.moveTo(x, y, duration = .01)
    pt.moveTo(x + 90, y - 40, duration = .01)
    sleep(0.01)
    pt.tripleClick()
    sleep(0.01)
    pt.rightClick()
    pt.moveRel(20,-130, duration=0.01)
    sleep(0.01)
    pt.click()
    whatssapp_message = pyperclip.paste()
    return whatssapp_message


#post response

def post_response(message) :
    pt.moveTo(x + 200, y + 25, duration = .01)
    pt.click()
    pt.typewrite(message, interval=.001)

    pt.typewrite("\n")                  #sending the message \n is interpreted as enter to newline character




post_response(get_message())
