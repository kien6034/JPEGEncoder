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

# image = Image.open("input.jpg")
# witdh, height = image.size

# print(f" original width and hegiht is: {witdh}, {height}")

# #resize image. make image chia het cho 8
# if witdh % 8 !=0 or height % 8 !=0:
#   image = image.resize((witdh - witdh%8,height - height%8))
#   witdh, height = image.size

# rImage,gImage,bImage = image.convert('RGB').split()
# rMat = numpy.asarray(rImage).astype(int)
# gMat = numpy.asarray(gImage).astype(int)
# bMat = numpy.asarray(bImage).astype(int)

# #shift
# rMat = rMat - 128
# gMat = gMat - 128
# bMat = bMat - 128

# Quant_50 = [
#   [16, 11, 10, 16, 24, 40, 51, 61],
#   [12, 12, 14, 19, 26, 58, 60, 55],
#   [14, 13, 16, 24, 40, 57, 69, 56],
#   [14, 17, 22, 29, 51, 87, 80, 62],
#   [18, 22, 37, 56, 68, 109, 103, 77],
#   [24, 35, 55, 64, 81, 104, 113, 92],
#   [49, 64, 78, 87, 103, 121, 120, 101],
#   [72, 92, 95, 98, 112, 100, 103, 99]
# ]

# zigzagOrder = numpy.array([0,1,8,16,9,2,3,10,17,24,32,25,18,11,4,5,12,19,26,33,40,48,41,34,27,20,13,6,7,14,21,28,35,42,
#                            49,56,57,50,43,36,29,22,15,23,30,37,44,51,58,59,52,45,38,31,39,46,53,60,61,54,47,55,62,63])

# Cos_table = [
#   [math.cos((2*i+1)*j * math.pi/16) for j in range(8)] for i in range(8)
# ]

# Range_list = [(i,j) for i in range(8) for j in range(8)]
# Root2_inv = 1 / math.sqrt(2)

# #RLE encoder - ma hoa nhung con sat nhau
# def rle(input):
#   encodeRLE = ""
#   p = 0  
#   while (p < 63):
#     count = 1
#     ch = input[p]
#     q = p
#     while (q < 63):
#       if input[q] == input[q+1]:
#         count += 1
#         q += 1
#       else:
#         break
#     encodeRLE = encodeRLE +" "+ str(count) + " " + str(ch)
#     p = q + 1
#   return encodeRLE

# #compute pixels
# pixels = int(witdh * height /64)

# rMat0 = rMat.flatten()
# gMat0 = gMat.flatten()
# bMat0 = bMat.flatten()

# #split array into 64-elements arrays
# rMat1 = numpy.array_split(rMat0, pixels)
# gMat1 = numpy.array_split(gMat0, pixels)
# bMat1 = numpy.array_split(bMat0, pixels)

# #reshape arrays to 8x8 blocks
# for m in range(pixels):
#   rMat1[m] = rMat1[m].reshape(8,8)

# #compute DCT 
# for m in range(pixels):
#   for u in range (8):
#     for v in range (8):
#       r = 0
#       for i,j in Range_list:
#         r += rMat1[m][i][j] * Cos_table[i][u] * Cos_table[j][v]
#       if u == 0: r *= Root2_inv
#       if v == 0: r *= Root2_inv
#       rMat1[m][u][v] = r*1/4 


# for m in range(pixels):
#   #Quantization
#   rMat1[m] = numpy.rint(rMat1[m]/Quant_50)    
#   rMat1[m] = rMat1[m].reshape([64])[zigzagOrder].astype(int)

# for m in range (pixels):
#   encodedStr = rle(rMat1[m])
#   f = open("z.txt", "a")
#   f.write(encodedStr)



# for m in range(pixels):
#   gMat1[m] = gMat1[m].reshape(8,8)

# for m in range(pixels):
#   for u in range (8):
#     for v in range (8):
#       r = 0
#       for i,j in Range_list:
#         r += gMat1[m][i][j] * Cos_table[i][u] * Cos_table[j][v]
#       if u == 0: r *= Root2_inv
#       if v == 0: r *= Root2_inv
#       gMat1[m][u][v] = r*1/4 


# for m in range(pixels):
#   gMat1[m] = numpy.rint(gMat1[m]/Quant_50)    
#   gMat1[m] = gMat1[m].reshape([64])[zigzagOrder].astype(int)

# for m in range (pixels):
#   encodedStr = rle(rMat1[m])
#   f = open("z.txt", "a")
#   f.write(encodedStr)

# for m in range(pixels):
#   bMat1[m] = bMat1[m].reshape(8,8)

# for m in range(pixels):
#   for u in range (8):
#     for v in range (8):
#       r = 0
#       for i,j in Range_list:
#         r += bMat1[m][i][j] * Cos_table[i][u] * Cos_table[j][v]
#       if u == 0: r *= Root2_inv
#       if v == 0: r *= Root2_inv
#       bMat1[m][u][v] = r*1/4 

# for m in range(pixels):
#   bMat1[m] = numpy.rint(bMat1[m]/Quant_50)   
#   bMat1[m] = bMat1[m].reshape([64])[zigzagOrder].astype(int)

# for m in range (pixels):
#   encodedStr = rle(rMat1[m])
#   f = open("z.txt", "a")
#   f.write(encodedStr)




def FindFrequency(input):
  inputs = [2, 3, 5, 2, 6, 8, 5, 4, 2, 4, 9]
  fl = dict()
  f = open(input, 'r')

  for x in f.read().split():
    if x not in fl:
      
      fl[x] = 1
    else:
     
      fl[x] +=1
      
  return fl, f.read().split()

def createTree():
  frequency, inputs = FindFrequency('z.txt')
  frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
  huffman = Huffman(frequency)
  nodes = huffman.sort()

  huffmanCode = huffman.huffman_code_tree(nodes[0][0])
  
  huffman.printCode(inputs, huffmanCode)




def main():
    inputFile = "input.jpg"

    createTree()

if __name__ == "__main__":
    main()