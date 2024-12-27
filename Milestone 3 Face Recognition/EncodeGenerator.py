import cv2

import pickle
import os

folderPath = 'Images'
modePathList = os.listdir(folderPath)
imgList = []
for Path in modePathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
print(len(imgList))