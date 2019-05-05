"""
high level support for doing this and that.
"""
import cv2

import numpy as np

from matplotlib import pyplot as plt

from scipy import misc

from PIL import Image

IMG = cv2.imread('lena_gray_8.tif', 0)

_8by8BitPlanes = np.zeros((8, 8, 8))
# print(_8by8BitPlanes)

for rowIndex, row in enumerate(IMG):
    for colIndex, col in enumerate(row):
        # print(int(bincol, 2))
        bincol = format(col, '08b')
        for bitPlaneIndex, bitPlane in enumerate(bincol):

            _8by8BitPlanes[len(bincol) - 1 -
                           bitPlaneIndex][rowIndex][colIndex] = bitPlane

# print(IMG)

print(_8by8BitPlanes[7])
"""
Logic for run length coding
"""

#histo = plt.hist(img.ravel(),256,[0,256]); plt.show()
# hist,bins = np.histogram(img.ravel(),256,[0,256])

# max1=0
# for i in range(0,256):
# 	if max1 < hist[i]:
# 		max1=hist[i]
# 		a=i
# min1=15654

# for j in range(0,256):
# 	if min1 >= hist[j]:
# 		min1=hist[j]
# 		b=j

# print(hist)
# print(img)
# print('a=',a)
# print('b=',b)
# print('min1=',min1)
# print('max1=',max1)

# lena = misc.imread('lena_gray_512.tif','L')
# print(lena.shape)
# embed = np.zeros(shape=(512,512))

# for i in range(512):
# 	for j in range(512):
# 		embed[i][j]=lena[i][j]

# for i in range(512):
# 	for j in range(512):
# 		if embed[i][j]>156 and embed[i][j]<255:
# 			embed[i,j] = embed[i][j]+1

# #print(embed)

# strp="hello" #secret message
# m =''.join(format(ord(x),'08b') for x in strp)
# print('m=',m,len(m))
# #print(b[0])
# #
# #def str_to_bin(string):
# #	l=list(string)
# #	a=''
# #	for i in l:
# #		a=a+format(ord(i),'08b')
# #	print('a=',a[1],m[1])
# #
# #str_to_bin("hello")

# #print(m)
# #print(len(m))

# #for i in range(35):
# 	#print(m[i])
# #print(m[0])

# ind=0
# for i in range(512):
# 	for j in range(512):
# 		if(embed[i][j]==156):
# 			if ind == len(m):
# 				break
# 			if m[ind] == m[1]:
# 				#print('hello')
# 				ind=ind+1
# 				embed[i][j]=embed[i][j]+1

# 			else:
# 				#print('hi')
# 				ind=ind+1

# if(embed[i][j]==157):
#     print('Hi')
# #print('Hi)
# #print(embed)

# imgl= Image.fromarray(embed).convert('L')
# imgl.save('my.png')
# #imgl.show()
