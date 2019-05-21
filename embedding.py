"""
high level support for doing this and that.
"""
import cv2

import numpy as np

from matplotlib import pyplot as plt

from scipy import misc

from PIL import Image

import runlengthcoding

# outputFile = open('output.txt', 'w')
IMG = cv2.imread('lena_gray_8.tif', 0)

_8by8BitPlanes = np.zeros((8, 8, 8), dtype=int)

ROW_BY_ROW = 1
COLUMN_BY_COLUMN = 2
# print(_8by8BitPlanes)

for rowIndex, row in enumerate(IMG):
    for colIndex, col in enumerate(row):
        # print(int(bincol, 2))
        bincol = format(col, '08b')
        for bitPlaneIndex, bitPlane in enumerate(bincol):

            _8by8BitPlanes[len(bincol) - 1 -
                           bitPlaneIndex][rowIndex][colIndex] = bitPlane

# print(IMG)

# print(_8by8BitPlanes[0])
"""
Logic for BMPR Scheme to compress the bit planes
There are four BMPR Scheme 00, 01, 10, 11
"""


def generateBMPRScheme(arr, bitType, blockType):
    whichScheme = ''
    if blockType == 0:
        whichScheme = 'Row by Row bit and block'
    elif blockType == 1:
        whichScheme = 'Row by Row bit and Column by Column block'
    elif blockType == 2:
        whichScheme = 'Column by Column bit and Row by Row block'
    elif blockType == 3:
        whichScheme = 'Column by Column bit and Column by Column block'
    # print('BMPRS Scheme ', whichScheme)
    # outputFile.write('BMPRS Scheme ' + whichScheme + '\n')

    firstBlock = arr[0:4, 0:4].flatten(bitType)
    firstBlock = getStringFromNP(firstBlock)
    # firstBlock = ''.join(map(str, firstBlock))
    # print('first block', firstBlock)

    # outputFile.write('first block ' + str(firstBlock) + '\n')
    secondBlock = ''
    thirdBlock = ''
    FourthBlock = ''
    if blockType == 0 or blockType == 2:
        secondBlock = arr[0:4, 4:8].flatten(bitType)
        secondBlock = getStringFromNP(secondBlock)
        # print('second block', secondBlock)
        # outputFile.write('second block ' + str(secondBlock) + '\n')
        thirdBlock = arr[4:8, 0:4].flatten(bitType)
        thirdBlock = getStringFromNP(thirdBlock)
        # print('third block', thirdBlock)
        # outputFile.write('third block ' + str(thirdBlock) + '\n')

    elif blockType == 1 or blockType == 3:
        secondBlock = arr[4:8, 0:4].flatten(bitType)
        secondBlock = getStringFromNP(secondBlock)
        # print('second block', secondBlock)

        # outputFile.write('second block ' + str(secondBlock) + '\n')

        thirdBlock = arr[0:4, 4:8].flatten(bitType)
        thirdBlock = getStringFromNP(thirdBlock)
        # print('third block', thirdBlock)
        # outputFile.write('third block ' + str(thirdBlock) + '\n')

    fourthBlock = arr[4:8, 4:8].flatten(bitType)
    fourthBlock = getStringFromNP(fourthBlock)
    # print('fourth block ', fourthBlock)
    # outputFile.write('fourth block ' + str(FourthBlock) + '\n')
    BMPRcode = firstBlock + secondBlock + thirdBlock + fourthBlock
    # print(firstBlock, secondBlock, thirdBlock, FourthBlock)
    # for ele in blockArr:
    #     BMPRcode = BMPRcode + ele

    return BMPRcode


def getBMPRScheme(arr, schemeType):
    # print('in get BMPR Scheme')
    if schemeType == 0:
        return generateBMPRScheme(arr, 'C', 0)
    elif schemeType == 1:
        return generateBMPRScheme(arr, 'C', 1)
    elif schemeType == 2:
        return generateBMPRScheme(arr, 'F', 2)
    else:
        return generateBMPRScheme(arr, 'F', 3)


def getStringFromNP(arr):
    return ''.join(map(str, arr))


for bitPlane in _8by8BitPlanes:
    print('bit plane ', bitPlane)
    # outputFile.write('bit plane \n' + str(bitPlane) + '\n')
    i = 0
    while i < 4:
        dataInBitPlane = getBMPRScheme(bitPlane, i)
        encodedData = runlengthcoding.encodeRun(dataInBitPlane)
        print(dataInBitPlane, encodedData)
        i = i + 1

# print('switch output ', getBMPRScheme(_8by8BitPlanes[0], 0))
"""
Logic for run length coding
"""
