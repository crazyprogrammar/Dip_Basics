#Web Camera Image Picture
#Matplots and colormaps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    cap=cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame=cap.read()
        print(ret)
        print(frame)
    else:
        ret=False;
        
    
    img1=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.imshow(img1)
    plt.title("Web Camera")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
    
    cap.isrelease()
    
    
    
    
    
if __name__ == "__main__":
    main()    