import os
import xml.etree.ElementTree as ET, numpy as np
import numpy as np
allList = np.load('xml.npy')
allList = allList.tolist()
#print(len(allList))]
allCategories = list()
allAlpha = list()
num = 0

for i in range(len(allList)):
    dic = allList[i]
    allSquare = list()
    allPoint = list()
    alpha = list()

    for j in range(dic['num']):
        cat = dic['cat'+str(j+1)]
        bbox = dic['bbox' + str(j+1)]
        square = int(bbox[2])*int(bbox[3])
        point = [int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])]
        allSquare.append(square)
        allPoint.append(point)

    for j in range(dic['num']-1):
        for k in range(j+1,dic['num']):
            width = allPoint[j][2] + allPoint[k][2] - max(allPoint[k][0]+allPoint[k][2],allPoint[j][0]+allPoint[j][2]) + min(allPoint[k][0],allPoint[j][0])
            height = allPoint[j][3] + allPoint[k][3] - max(allPoint[k][1]+allPoint[k][3],allPoint[j][1]+allPoint[j][3]) + min(allPoint[k][1],allPoint[j][1])
            if (width <=0 or height <=0):
                a = 0
                alpha.append(a)
            else:
                a = (width*height)*1.0/min(allSquare[j],allSquare[k])
                a = round(a,3)
                alpha.append(a)
#           print j,k,a
#    print alpha
    allAlpha.append(alpha)
#    print avgAlpha

for i in range(0,len(allList),20):
    print allList[i]['name'],allAlpha[i]
