import colorchange as color
import joblib

allDic={}
model = joblib.load('model-x7.pkl')
num=0.3
#file1 = open("allColors.py","w")
file1 = open("allColors.txt","a")
cont=0
total=255*255*255
for r in range(256):
    for g in range(256):
        for b in range(256):
            strDic=str(r)+","+str(g)+","+str(b)
            rgb=(r,g,b)
            #allDic[strDic]=color.modify_rgb(rgb,model,1+num,0.5)
            print(str(cont*100/total)+"%")
            r1,g1,b1=color.modify_rgb(rgb,model,1+num,0.5)
            file1.write(strDic+":"+str(r1)+","+str(g1)+","+str(b1)+"\n")
            cont=cont+1           

#file1.write(str(allDic))
file1.close()
