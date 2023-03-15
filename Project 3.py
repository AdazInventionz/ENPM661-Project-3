#!/usr/bin/env python
# coding: utf-8

# In[17]:


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
    
    #Both Rectangles
    for x in range(100, 151):
        
        for y in range(0, 250):
            
            if y < 100 or y >= 150:
                arena[y, x] = white
                
    #Pentagon (Left Half)
    for x in range(235, 301):
        
        for y in range(0, 250):
            
            if (y >= (-38/65)*x + (2930/13)) and (y <= (38/65)*x + (320/13)):
                arena[y, x] = white
                
    #Pentagon (Right Half)
    for x in range(300, 366):
        
        for y in range(0, 250):
            
            if (y >= (38/65)*x + (-1630/13)) and (y <= (-38/65)*x + (4880/13)):
                arena[y, x] = white
    
    #Triangle
    for x in range(460, 511):
        
        for y in range (0, 250):
            
            if (y >= 2*x - 895) and (y <= -2*x + 1145):
                arena[y, x] = white
    
arena = np.zeros((250, 600, 3), dtype = "uint8")
setup()
cv.imshow("Arena", arena)
cv.waitKey()
cv.destroyAllWindows()


# In[ ]:





# In[ ]:




