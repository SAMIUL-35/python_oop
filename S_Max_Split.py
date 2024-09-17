import pyautogui
import time

# Get the height of the pyramid
n = int(input("Enter the height of the pyramid: "))

# Inform the user to switch to the text editor
print("You have 5 seconds to switch to your text editor...")
time.sleep(5)

def type_pyramid(n):
    for i in range(n):
 
       

        
      
        pyautogui.typewrite('#' * (i + 1),interval=0.25)
        
        
        pyautogui.press('enter')


type_pyramid(n)
#
##
###
####
#####
