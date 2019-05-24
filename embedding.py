"""
high level support for doing this and that.
"""
import cv2

import numpy as np

from matplotlib import pyplot as plt

from scipy import misc

from PIL import Image

import math

import runlengthcoding

# outputFile = open('output.txt', 'w')
IMG = cv2.imread('lena_gray_32.tif', 0)
width, height = IMG.shape[:2]
blockSize = int(math.sqrt((width * height) / 4))
NOOFBITCOMPRESSED = 2
# print(width, height, blockSize)

_8by8BitPlanes = np.zeros((8, width, height), dtype=int)

_8by8BitCompressedBitPlanes = np.zeros((8, width, height), dtype=int)

binBlockSize = format(blockSize, '05b')
binLFIX = format(runlengthcoding.LFIX, '03b')
bitNoOfBitCompressed = format(NOOFBITCOMPRESSED, '02b')
print(binBlockSize, binLFIX, bitNoOfBitCompressed)
exit()

# print(binBlockSize)

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

    firstBlock = arr[0:blockSize, 0:blockSize].flatten(bitType)
    firstBlock = getStringFromNP(firstBlock)
    # firstBlock = ''.join(map(str, firstBlock))
    # print('first block', firstBlock)

    # outputFile.write('first block ' + str(firstBlock) + '\n')
    secondBlock = ''
    thirdBlock = ''
    FourthBlock = ''
    if blockType == 0 or blockType == 2:
        secondBlock = arr[0:blockSize, blockSize:2 *
                          blockSize].flatten(bitType)
        secondBlock = getStringFromNP(secondBlock)
        # print('second block', secondBlock)
        # outputFile.write('second block ' + str(secondBlock) + '\n')
        thirdBlock = arr[blockSize:2 * blockSize, blockSize:2 *
                         blockSize].flatten(bitType)
        thirdBlock = getStringFromNP(thirdBlock)
        # print('third block', thirdBlock)
        # outputFile.write('third block ' + str(thirdBlock) + '\n')

    elif blockType == 1 or blockType == 3:
        secondBlock = arr[blockSize:2 *
                          blockSize, 0:blockSize].flatten(bitType)
        secondBlock = getStringFromNP(secondBlock)
        # print('second block', secondBlock)

        # outputFile.write('second block ' + str(secondBlock) + '\n')

        thirdBlock = arr[0:blockSize, blockSize:2 * blockSize].flatten(bitType)
        thirdBlock = getStringFromNP(thirdBlock)
        # print('third block', thirdBlock)
        # outputFile.write('third block ' + str(thirdBlock) + '\n')

    fourthBlock = arr[blockSize:2 * blockSize, blockSize:2 *
                      blockSize].flatten(bitType)
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


for bitPlane in np.flip(_8by8BitPlanes):
    bitPlaneIn1D = bitPlane.flatten()
    # print('bit plane ', bitPlane.flatten())
    encodedData = runlengthcoding.encodeRun(getStringFromNP(bitPlaneIn1D))
    # print(len(bitPlaneIn1D), len(encodedData))
    # outputFile.write('bit plane \n' + str(bitPlane) + '\n')
    i = 0
    while i < 4:
        dataInBitPlane = getBMPRScheme(bitPlane, i)
        encodedData = runlengthcoding.encodeRun(dataInBitPlane)
        decodedData = runlengthcoding.decodeRun(encodedData)
        print(len(dataInBitPlane), len(encodedData))
        # print(dataInBitPlane == decodedData)
        i = i + 1
    print('\n')
