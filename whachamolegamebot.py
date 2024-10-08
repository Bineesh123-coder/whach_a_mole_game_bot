# https://www.classicgame.com/game/Whack+a+Mole

#import 
import cv2
import pyautogui
import time

#No cooldown time
pyautogui.PAUSE=0

#template
template =cv2.imread('/home/tacodi/python opencv/whackabot/noiseimg.png')
template_gray=cv2.cvtColor(template,cv2.COLOR_RGB2GRAY)
template_w,template_h =template_gray.shape[::-1]


# game window dimensions
x,y,w,h =400,325,1031,977

#wait
time.sleep(3)

while True:
    #screenshot
    pyautogui.screenshot('/home/tacodi/python opencv/whackabot/image.png',(x,y,w,h))
    image=cv2.imread('/home/tacodi/python opencv/whackabot/image.png')
    
    while True:
        
        #show what the computer sees
        image_mini =cv2.resize(
            src =image,
            dsize =(500,500) # must be integer ,not flaot
        )
        cv2.imshow("Vision Window", image_mini)
        key=cv2.waitKey(10)
        if key == 27:  # Escape key to exit
           break
        cv2.destroyAllWindows()
        
        
        
        image_gray =cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
        result=cv2.matchTemplate(
            image = image_gray,
            templ =template_gray,
            method= cv2.TM_CCOEFF_NORMED
                                )
        min_val, max_val, min_loc, max_loc =cv2.minMaxLoc(result)
        print(f"Max Value: {max_val}, Max Location: {max_loc}")

        #threshold
        if max_val >=0.8:
            pyautogui.click(
                x=max_loc[0]+x, #screen x
                y=max_loc[1]+y #screen y
            )
            print(x,y)
            time.sleep(0.1)  # Small delay
            image= cv2.rectangle(
                img=image,
                pt1 = max_loc,
                pt2 = (
                    max_loc[0]+template_w, # =pt2 x
                    max_loc[1]+template_h #=pt2 y
                ),
                color=(0,0,255),
                thickness= -1 #fill the rectangle
            )
        
           
    
    



