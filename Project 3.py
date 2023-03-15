#!/usr/bin/env python
# coding: utf-8

# In[29]:


#Imported libraries
import numpy as np
import cv2 as cv
import time

#Sets up arena with obstacles
def setup():

    global arena
    
    #Colors
    white = (255, 255, 255)
    gray = (177, 177, 177)
    
    #Draw Obstacles
    for x in range(0, 600):

        for y in range(0, 250):
        
            if checkObstacle(x, y):
                arena[y, x] = (255, 255, 255)
                
#Checks to see if a node is an obstacle (or its border)
def checkObstacle(x, y):
    
    #Both Rectangles
    if x >= 100 and x <= 150:
        
        if y < 100 or y >= 150:
            return True
    
    #Pentagon (Left Half)
    if x >= 235 and x <= 300:
        
        if (y >= (-38/65)*x + (2930/13)) and (y <= (38/65)*x + (320/13)):
            return True
    
    #Pentagon (Right Half)
    if x >= 300 and x <= 366:
        
        if (y >= (38/65)*x + (-1630/13)) and (y <= (-38/65)*x + (4880/13)):
            return True
    
    #Triangle
    if x >= 460 and x <= 510:
        
        if (y >= 2*x - 895) and (y <= -2*x + 1145):
            return True
        
    return False
  
    
    
    
    
#Main Code
arena = np.zeros((250, 600, 3), dtype = "uint8")
        
setup()
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:




