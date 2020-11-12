from joblib import load
from cv2 import imread
from cv2 import imwrite
from numpy import shape
from numpy import hstack
from numpy import vstack


from colorchange import modify_rgb

from multiprocessing import Pool
from sys import argv
from os import makedirs
from os import rename
from time import time
from shutil import rmtree


colors={}
 
def removeTemp():
    """
        eliminaTemporales
    """
    rmtree('temporal/')

def dictionary(fileName):
    """
        procesamiento de imagen
    """
    model = load('model-x7.pkl')
    subimage=fileName
    h,w,bpp = shape(subimage)
    for pixelY in range(h):
        for pixelX in range(w):
                blue=subimage[pixelY][pixelX][0]
                green=subimage[pixelY][pixelX][1]
                red=subimage[pixelY][pixelX][2] 
                rgbTuple = (red,green,blue)
                if rgbTuple in colors.keys():
                    red,green,blue=colors[rgbTuple]
                else:
                    red,green,blue=modify_rgb(rgbTuple,model,1.025,1)
                    colors[rgbTuple]=(red,green,blue)
                subimage[pixelY][pixelX][0]=blue
                subimage[pixelY][pixelX][1]=green
                subimage[pixelY][pixelX][2]=red
    return subimage

def combine(fileName,newName):
    """
        combinar imagen inicial y final
    """
    originalImg=imread(fileName)
    newImage=imread(newName)
    horizontal = hstack((originalImg, newImage))
    combined=fileName.split(".")
    combined="c-"+combined[0]+"."+combined[1]
    imwrite(combined,horizontal)
    return combined

def pasteImg(arrDeImagen,newName):
    """
        combina las 4 partes de la imagen
    """    
    topSubimages = hstack((arrDeImagen[0], arrDeImagen[1]))
    bottomSubimages = hstack((arrDeImagen[2], arrDeImagen[3]))
    completeImage=vstack((topSubimages,bottomSubimages))
    imwrite(newName,completeImage)

def multiprocess(subimgArr):
    """
        funcion que se encarga del multiprocesamiento
    """
    with Pool(4) as p:
        subimgArr=p.map(dictionary,subimgArr)
    return subimgArr

def cutImg(imagen):
    """
        Parte la imagen en 4 subimagenes
    """
    originalImage=imread(imagen)
    h,w,bpp = shape(originalImage)
    subimageTopLeft = originalImage[: h//2, :w//2]
    subimageTopRigth = originalImage[: h//2, w//2:w]
    subimageBottomLeft = originalImage[h//2: h, :w//2]
    subimageBottomRigth = originalImage[h//2: h, w//2:w]
    
    return [subimageTopLeft,subimageTopRigth,subimageBottomLeft,subimageBottomRigth]
   

if __name__ == "__main__":
    start_time = time()
    fileName = str(argv[1])
    fileName=fileName.split('\\')[-1]
    newDir=fileName.split(".")[0]
    try:
        makedirs("temporal/")
        makedirs("pruebas/"+newDir)
    except:
        cont=0
        done=False
        while(not done):
            try:
                newDir=newDir+"("+str(cont)+")"
                makedirs("pruebas/"+newDir)
                done=True
            except :
                cont+=1  
    arrImg=cutImg(fileName)
    arrImg=multiprocess(arrImg)
    newName="temporal/new-"+fileName
    pasteImg(arrImg,newName)
    #combined=combine(fileName,newName)
    rename(newName,"pruebas/"+newDir+"/new-"+fileName)
    #rename(combined,"pruebas/"+newDir+"/"+combined)
    #f=open("time.txt","a")
    #f.write(str((time() - start_time)*1000.0)+"\n")
    #f.close()
    print("-- %s seconds --" %(time() - start_time))
    removeTemp()