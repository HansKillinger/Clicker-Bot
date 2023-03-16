from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from time import sleep

keyboard = KeyboardController()
mouse = MouseController()

### Keyboard controls
# keyboard.press(Key.ctrl)
# keyboard.press('c')
# keyboard.release('c')
# keyboard.release(Key.ctrl)
# keyboard.type('Message to type')

### Read Mouse Pos
# print ("Current position: " + str(mouse.position))

### Set Mouse Pos
# mouse.position = (10, 20)

### Click the left button
# mouse.click(Button.left, 1)

### Click the right button
# mouse.click(Button.right, 1)

### Click the middle button
# mouse.click(Button.middle, 1)

### Double click the left button
# mouse.click(Button.left, 2)

### Click the left button ten times
# mouse.click(Button.left, 10)

# mouse.press(Button.left)
# mouse.release(Button.left)

### Scroll up two steps
# mouse.scroll(0, 2)
### Scroll right five steps
# mouse.scroll(5, 0)

##########MAIN SCRIPT############

x = 0
nft = 1
total = 1005
#while x < 1:
#    print("Current position: " + str(mouse.position))
sleep(5)
while nft <= total:
    # Searchbar
    mouse.position = (775, 620)
    sleep(.1)
    mouse.click(Button.left, 1)
    sleep(14)
    mouse.position = (1030, 205)
    sleep(.1)
    mouse.click(Button.left, 1)
    sleep(.5)
    nft += 1
    print(str(nft) + ' of ' + str(total))
exit()

