import numpy as np
import cv2
import colorchange as color
import sys
import os
from sklearn.preprocessing import PolynomialFeatures
import joblib


def pixcelXpixcel(fileName,num,pipe):
    m=cv2.imread(fileName)
    h,w,bpp = np.shape(m)
    num=num/10
    #cv2.imshow('old', m)
    total=h*w
    cont=0
    for py in range(0,h):
        for px in range(0,w):
                b=m[py][px][0]
                g=m[py][px][1]
                r=m[py][px][2] 
                rgb = (r,g,b)
                #print("-1:",end=" ")
                #print(rgb)
                r,g,b=color.modify_rgb(rgb,1+num,pipe)
                m[py][px][0]=b
                m[py][px][1]=g
                m[py][px][2]=r
                cont+=1
                print(str(cont*100/total)+"%")
    #cv2.imshow('new', m)
    cv2.waitKey(0)
    
    newName=fileName.split(".")
    newName="new-"+str(num)+"-"+newName[0]+"."+newName[1]
    cv2.imwrite(newName,m)
    return newName

def combinar(fileName,newName,num):
    m=cv2.imread(fileName)
    m1=cv2.imread(newName)
    numpy_horizontal = np.hstack((m, m1))
    combinado=fileName.split(".")
    num=num/10
    combinado="c-"+str(num)+"-"+combinado[0]+"."+combinado[1]
    cv2.imwrite(combinado,numpy_horizontal)
    return combinado

if __name__ == "__main__":
    fileName = str(sys.argv[1])
    fileName=fileName.split('\\')[-1]
    newDir=fileName.split(".")[0]+"/"
    os.makedirs(newDir)
    newNames=[]
    pipe = joblib.load('model-x6.pkl')
    for i in range(1,11):
        newName=pixcelXpixcel(fileName,i,pipe)
        combinado=combinar(fileName,newName,i)
        os.rename(newName,newDir+newName)
        os.rename(combinado,newDir+combinado)