import pyautogui as pt 
from time import sleep 
import pyperclip
import random 

sleep(2)

position1 = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence = .6)         # confidence is the acceptable look alikeness of the picture
x = position1[0]
y = position1[1]

# Gets message

def get_message():
    global x, y

    position = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence = .6)
    x = position1[0]
    y = position1[1]

    pt.moveTo(x, y, duration = .5)
    pt.moveTo(x + 70, y - 40, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,-130)
    pt.click()
    whatssapp_message = pyperclip.paste()
    print("Message recieved : "+ whatssapp_message)

    return whatssapp_message


#post response

def post_response(message) :
    global x,y
    position = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence = .6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 25, duration = .5)
    pt.click()
    pt.typewrite(message, interval=.01)

    position_send = pt.locateOnScreen("images/send.JPG", confidence = .9)
    pt.moveTo(position_send[0] + 20 ,position_send[1] + 20, 0.5)
    pt.click()




post_response(get_message())
