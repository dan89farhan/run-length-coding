from PIL import Image
from collections import Counter
import heapq

# Image details and initialization of variables
end = 255
img = Image.open('lena_gray_512.tif')
print(img)
print(type(img))
pix_val =  list(img.getdata())
img_width, img_height = img.size
freq_count = Counter(pix_val) # pix values of the image being stored in a list

# Histogram of the image and max_pix and min_pix values
hist = img.histogram() 
print('histogram ',len(hist))
max_p = hist.index(max(hist)) 
min_p = hist[end:max_p:-1].index(min(hist))
min_p = end - min_p
print(max_p,min_p)
print(hist[max_p],hist[min_p])