import matplotlib.pyplot as plt
import PIL
import numpy 
import scipy
import math
from PIL import Image
from matplotlib.pyplot import imread
from numpy import zeros
from numpy import r_
from scipy import fftpack
from numpy import pi
import sys
from huffman import *

class Extracter():
    def __init__(self, image, QUANT_50, ZIGZAG_ORDER, COS_TABLE, RANGE_LIST):
        self.image = image
        self.width = image.size
        self.height = image.size
        self.rMat = []
        self.gMat = []
        self.bMat = []
        self.pixels = 0
        self.QUANT_50 = QUANT_50
        self.ZIGZAG_ORDER = ZIGZAG_ORDER
        self.COS_TABLE = COS_TABLE
        self.RANGE_LIST = RANGE_LIST
        self.ROOT2_INV = 1 / math.sqrt(2)

    def resize(self):
        if self.width %8 != 0 or self.height %8 != 0:
            self.image = self.image.resize((self.width - self.width%8, self.height - self.height%8))
            self.width, self.height = self.image.size

    def seperateRGB(self):
        rImage,gImage,bImage = self.image.convert('RGB').split()
        #separtea image into 3 arrays according to r,g b value
        self.rMat = numpy.asarray(rImage).astype(int) - 128
        self.gMat = numpy.asarray(gImage).astype(int) - 128
        self.bMat = numpy.asarray(bImage).astype(int) - 128

    def rle(self, input):
        encodeRLE = ""
        p = 0  
        while (p < 63):
            count = 1
            ch = input[p]
            q = p
            while (q < 63):
            if input[q] == input[q+1]:
                count += 1
                q += 1
            else:
                break
            encodeRLE = encodeRLE +" "+ str(count) + " " + str(ch)
            p = q + 1
        return encodeRLE
    
    def split_to_array64(self):
        self.pixels = int(self.width * self.height /64)

        rMat0 = rMat.flatten()
        gMat0 = gMat.flatten()
        bMat0 = bMat.flatten()

        #split array into 64-elements arrays
        self.rMat = numpy.array_split(rMat0, pixels)
        self.gMat = numpy.array_split(gMat0, pixels)
        self.bMat = numpy.array_split(bMat0, pixels)

        #reshape to 8x8 block
        for m in range(self.pixels):
            self.rMat[m] = self.rMat[m].reshape(8,8)
    
    def dct(self, Mat):
        for m in range(self.pixels):
            for u in range (8):
                for v in range (8):
                    r = 0
                    for i,j in self.RANGE_LIST:
                        r += Mat[m][i][j] * self.COS_TABLE[i][u] * self.COS_TABLE[j][v]
                    if u == 0: r *= self.ROOT2_INV
                    if v == 0: r *= self.ROOT2_INV
                    Mat[m][u][v] = r*1/4 
    
    def quantization(self):
        for m in range(self.pixels):
            self.rMat[m] = numpy.rint(self.rMat[m]/self.QUANT_50)
            self.rMat[m] = self.rMat[m].reshape([64])[self.ZIGZAG_ORDER].astype(int)

