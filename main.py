from replyengine import get_reply

import pyautogui as pt
import pyperclip
from time import sleep
from random import randint
import logging


#Defining logger

logging.basicConfig(filename='history.log', level= logging.INFO, format = '%(asctime)s:%(message)s' )


# Locating smiley and paperclip on screen as reference point


def locate_reference_point():  
    global x, y  

    position = pt.locateOnScreen("images/smiley_paperclip.JPG", confidence=0.6)
    
    if position != None:
        x, y = position[0], position[1]
    
    else:
        print("\nWhatsApp Web not open on the screen at the time of running the program. Reference point not found.\n")

        for i in range(3,0,-1):
            print("Retrying in {} seconds..".format(i))
            sleep(1)
        
        locate_reference_point()
        


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
    )  # used by both unread_msgs  and get_msg..Make it a single fx. This point changes with differennt screen sizes
    sleep(0.01)
    pt.tripleClick()
    sleep(0.01)
    whatsapp_message = copy_to_variable()
    return whatsapp_message


# Processing and Sending response

def post_response(whatsapp_message):     
    reply_message = get_reply("csv_dataset.txt", whatsapp_message)
    if  reply_message == None:
         reply_message = "No appropriate response found."
    else:
         reply_message =  reply_message[randint(0,1)]

    # Log messages and responses
    logging.info("\tMessage: {} \t Reply: {} ".format(whatsapp_message, reply_message))    
   
    pt.moveTo(x + 150, y + 25, duration=0.01)
    pt.click()
    sleep(0.1)
    pt.write(reply_message + "\n", interval=0)


if (
    __name__ == "__main__"
):  # Boilerplate __name__ guard for importing this module elsewhere
    sleep(3)    #meanwhile start up Web Whatsapp
    
    try:
        locate_reference_point()

    except Exception:
        print("WhatsApp Web not open on the screen at the time of running the program. Reference point not found.")
    
    else:
        post_response(get_message())



# move no appropriate response found into replyengine and add fillers.txt for this case.
# Instead of Global x, y, return positionxy 