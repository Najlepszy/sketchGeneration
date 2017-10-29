#coding=utf-8
import os
import xml.etree.ElementTree as ET, numpy as np
import scipy.io as sio
import csv

#统计info-06-04的类别信息和线条信息
imageNetId = []
stroke_count = []
with open('info-06-04\info\stats.csv','rb') as f:
    reader = csv.reader(f)
    for i,row in enumerate(reader):
        if i>=1:
            imageNetId.append(row[2])
            stroke_count.append(row[8])

np.save('imageNetId2.npy',imageNetId)
np.save('stroke_count2.npy',stroke_count)

#统计sketches_matlab的类别信息和线条信息
sketch_name =[]
sketch_stroke_count = []
sketches = sio.loadmat('sketches_matlab\sketches_matlab\sketches.mat')
# print sketches
for i in range(20000):
    sketch_name.append(i+1)
    sketch_stroke_count.append(sketches['D'][i][2].size - 8)

np.save('image_net_id1.npy',sketch_name)
np.save('stroke_count1.npy',sketch_stroke_count)

a= np.load('image_net_id2.npy')
print a
b = np.load('stroke_count2.npy')
print b
c = np.load('image_net_id1.npy')
print c
d = np.load('stroke_count1.npy')
print d
