import numpy as np
import cv2
import colorchange as color
import sys
import os
from sklearn.preprocessing import PolynomialFeatures
import joblib
import time


def pixcelXpixcel(fileName,num,model):
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
                r,g,b=color.modify_rgb(rgb,model,1+num,0.5)
                m[py][px][0]=b
                m[py][px][1]=g
                m[py][px][2]=r
                cont+=1
                print(str(cont*100/total)+"%")
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
    start_time = time.time()
    fileName = str(sys.argv[1])
    fileName=fileName.split('\\')[-1]
    newDir=fileName.split(".")[0]
    os.makedirs("pruebas/"+newDir)
    newNames=[]
    model = joblib.load('model-x7.pkl')
    i=0.3
    newName=pixcelXpixcel(fileName,i,model)
    combinado=combinar(fileName,newName,i)
    os.rename(newName,"pruebas/"+newDir+"/"+newName)
    os.rename(combinado,"pruebas/"+newDir+"/"+combinado)
    print("--- %s seconds ---" % (time.time() - start_time))