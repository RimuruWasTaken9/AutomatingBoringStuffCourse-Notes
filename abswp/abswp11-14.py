import pyautogui

#moving mouse video

#in computing, 0,0 is the top left of the screen.
#x increases going right, y increases going down
print(pyautogui.size())
width, height = pyautogui.size() #size of screen resolution
print(width)
print(height)
print(pyautogui.position()) #gives position of mouse at that moment

#pyautogui.moveTo(10,10)#moves my mouse to near top right
#pyautogui.moveTo(10,10,duration =1.5)
#^^^ moves my mouse to near top right in 1.5 seconds

#pyautogui.moveRel(250,0,duration = 2)
#^^^ moves my mouse to the right in 2 seconds by 250
#pyautogui.moveRel(0,-100,duration = 1)
#^^^ moves my mouse up 100, its negative because y increases going down

#pyautogui.click(1430,62)
#left clicks at the specified position
#you could also do 'doubleClick', 'rightClick', or 'middleClick',etc


#pyautogui.click()
#this just clicks wherever the mouse currently is

#pyautogui.dragTo(200,0)
#this will click and hold to wherever the specified point is


#pyautogui.dragRel(200,0)
#this will click and hold my mouse 200 to the right

#if you ever lose control and can't control the mouse, slam it into
#the top left corner, if it is there for even a moment, an exception
#will get raised and the program will end


#pyautogui.displayMousePosition()
#^^^ This is fucking awesome, it gives your mouse coordinates real
#time as well as the color of the pixel you're over. This won't work
#in idle, well it will but it will look hideous. Run it in cmd
#through python
#-------------------------------------------------------------------

#moving keyboard video

#pyautogui will go to the window that currently has focus

#pyautogui.click() ; pyautogui.typewrite('Hellow world!')
#apparently you can seperate two lines with a semicolon
#this line of code clicks first, then adds text wherever you clicked


#pyautogui.typewrite('Hellow world!', interval = 0.2)
#interval means the amount of time inbetween writing each letter



#pyautogui.click() ; pyautogui.typewrite(['a','b','left','left','X','Y'],interval=.2)
#this clicks where your mouse is, then writes what is in the list
#the two 'left's are the arrow key left. so it goes left twice before
#finishing the rest of the list
#for some reason, if you use a list, it won't let you have more than
#one letter in each string


print(pyautogui.KEYBOARD_KEYS)
#gives you all the names of all the different keyboard keys you can use
#this is usually for keyboard shortcuts

#pyautogui.press('f1')
#.press is for pressing one specific key

#pyautogui.hotkey('ctrl','o')
#for passing a series of keys that you can use in combination


#-------------------------------------------------------------------

#screenshots and image recognition video

#print(pyautogui.screenshot())
#pyautogui.screenshot('c:\\users\\rimuru\\screenshot_example.png')
#.screenshot takes a screenshot, and stores it in the specified file location
#if there is a file with the same name ther it replaces it
'''
IGNORE THIS NOW, I FIXED THE ISSUE
#im.save('screenshot_example.png')
#.screenshot takes a screenshot, and stores it in the specified file location
#however, despite the tutorial, the code will give an error unless I add
# the .save line of code. The screenshot will still be taken and stored
#in the first file location, the program won't complain about the second
#line so long as its argument is a string and ends in a valid file extension
such as .png
'''


#print(pyautogui.locateOnScreen('c:\\users\\rimuru\\screenshot_example2.png'))
#use it to look at the screen and find a picture of the file in the argument
#it returns a list of 4 strings. The first two are the x and y coordinates
#of where it was found on the screen and the 3rd and 4th are the width
#and height of the image located
#this example was given a cropped version of my grad pic which was on screen
#the x and y values returned aren't the center, but the top right corner



#print(pyautogui.locateCenterOnScreen('c:\\users\\rimuru\\screenshot_example2.png'))
#this one returns the centered x and y value for the image

#pyautogui.moveTo(607,473,duration=2)
#this one moves to the center of that image by plugging in the cords


#the image matching needs to be PIXEL PERFECT
#if an image isn't found it returns the None value

#--------------------------------------------------------------------------

#combine all this shit for some awesome stuff







                                         
