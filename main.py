from replyengine import get_reply
from time import sleep

import pyautogui as pt
import pyperclip

# Locating smiley and paperclip on screen as refereence point


def locate_reference_point():  # none type object is not subscriptable in  x = po[0] as no object located. Use Try and Catch for such cases.
    global x, y #does running this function in another file again change the definition of x and y?

    position1 = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence=0.6)
    x = position1[0]
    y = position1[1]


# Function to copy onscreen highlighted text to a variable


def copy_to_variable():
    pt.hotkey("ctrl", "c")
    sleep(0.1)
    copied_msg = pyperclip.paste()
    return copied_msg


# Getting recieved message


def get_message():
    pt.moveTo(
        x + 82, y - 30, duration=0.01
    )  # used by both unread_msgs  and get_msg..make it a single fx. This point changes with differennt screen sizes
    sleep(0.01)
    pt.tripleClick()
    sleep(0.01)
    whatsapp_message = copy_to_variable()
    return whatsapp_message


# Processing and Sending response 

def post_response(message):
    message = get_reply("csv_dataset.txt",message)
    if message == None:
        message = "No appropriate response found."
    else :
        message = message[0]  +  message[1]    
    
    pt.moveTo(x + 150, y + 25, duration=0.01)
    pt.click()
    sleep(0.1)
    pt.write(message + "\n", interval=0.001)


if __name__ == "__main__" : # Boilerplate __name__ guard for importing this module elsewhere
    sleep(3)
    locate_reference_point()
    post_response(get_message())

