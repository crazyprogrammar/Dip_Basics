#Matplots and colormaps
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    
    
    imgpath="C:\Shreyas\OpenCv\modi.png"
    img=cv2.imread(imgpath,1)
    
    
    
    
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title("Modi in Mode BGR")
    plt.show()
    
    
    
    
    #Converted Image
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.title("Modi in Mode RGB")
    plt.show()

    
    
    
    
    
    
    
    
   # cv2.imshow('Modi',img)
   # cv2.waitKey(0)
   # cv2.destroyAllWindow('Modi')
    
if __name__ == "__main__":
    main()
