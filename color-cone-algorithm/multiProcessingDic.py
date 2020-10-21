import numpy as np
import cv2
import colorchange as color
import sys
import os
from sklearn.preprocessing import PolynomialFeatures
import joblib
from multiprocessing import Pool
import shutil
from functools import partial
import time
colores={}



    
def eliminarTemp():
    """
        eliminaTemporales
    """
    shutil.rmtree('temporal/')

def dictionary(fileName):
    """
        procesamiento de imagen
    """
    model = joblib.load('model-x7.pkl')
    i=0.3
    m=cv2.imread(fileName)
    h,w,bpp = np.shape(m)
    for py in range(0,h):
        for px in range(0,w):
                b=m[py][px][0]
                g=m[py][px][1]
                r=m[py][px][2] 
                rgb = (r,g,b)
                strDic=str(r)+","+str(g)+","+str(b)
                if strDic in colores.keys():
                    r,g,b=colores[strDic]
                else:
                    r,g,b=color.modify_rgb(rgb,model,1+i,0.5)
                    colores[strDic]=(r,g,b)
                m[py][px][0]=b
                m[py][px][1]=g
                m[py][px][2]=r
    cv2.waitKey(0)
    newName=fileName.split(".")
    newName=newName[0].split("/")
    newName="temporal/new-"+newName[1]+".png"
    cv2.imwrite(newName,m)
    return newName

def combinar(fileName,newName):
    """
        combinar imagen inicial y final
    """
    m=cv2.imread(fileName)
    m1=cv2.imread(newName)
    numpy_horizontal = np.hstack((m, m1))
    combinado=fileName.split(".")
    combinado="c-"+combinado[0]+"."+combinado[1]
    cv2.imwrite(combinado,numpy_horizontal)
    return combinado

def reconstruirImg(arrDeImagen,newName):
    """

    """
    m=cv2.imread(arrDeImagen[0])
    m1=cv2.imread(arrDeImagen[1])
    m2=cv2.imread(arrDeImagen[2])
    m3=cv2.imread(arrDeImagen[3])
    numpy_horizontal = np.hstack((m, m1))
    numpy_horizontal1 = np.hstack((m2, m3))
    numpy_vertical=np.vstack((numpy_horizontal,numpy_horizontal1))
    cv2.imwrite(newName,numpy_vertical)

def multiproceso():
    """
        funcion que se encarga del multiprocesamiento
    """
    arrDeImagen=['temporal/temp-0.png','temporal/temp-1.png','temporal/temp-2.png','temporal/temp-3.png']
    with Pool(4) as p:
        arrDeImagen=p.map(dictionary, arrDeImagen)
    return arrDeImagen

def partirImg(imagen):
    """
        Partir imagen
    """
    full_image=cv2.imread(imagen)
    h,w,bpp = np.shape(full_image)
    sub_image0 = full_image[0: h//2, 0:w//2]
    sub_image1 = full_image[0: h//2, w//2:w]
    sub_image2 = full_image[h//2: h, 0:w//2]
    sub_image3 = full_image[h//2: h, w//2:w]
    cv2.imwrite("temporal/temp-0.png",sub_image0)
    cv2.imwrite("temporal/temp-1.png",sub_image1)
    cv2.imwrite("temporal/temp-2.png",sub_image2)
    cv2.imwrite("temporal/temp-3.png",sub_image3)

if __name__ == "__main__":
    start_time = time.time()
    fileName = str(sys.argv[1])
    fileName=fileName.split('\\')[-1]
    newDir=fileName.split(".")[0]
    try:
        os.makedirs("temporal/")
        os.makedirs("pruebas/"+newDir)
    except:
        cont=0
        done=False
        while(not done):
            try:
                newDir=newDir+"("+str(cont)+")"
                os.makedirs("pruebas/"+newDir)
                done=True
            except :
                cont+=1  
    partirImg(fileName)
    arrDirc=multiproceso()
    newName="temporal/new-"+fileName
    reconstruirImg(arrDirc,newName)
    newName="temporal/new-"+fileName
    combinado=combinar(fileName,newName)
    os.rename(newName,"pruebas/"+newDir+"/new-"+fileName)
    os.rename(combinado,"pruebas/"+newDir+"/"+combinado)
    eliminarTemp()
    print("--- %s seconds ---" % (time.time() - start_time))