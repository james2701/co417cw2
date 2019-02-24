from PNM import *


#set gamma here
gamma = 2.2
n = 0
def g(x, gamma):
    x = x**(1/gamma)
    x[x>1] = 1.0
    return x
#load data
data = loadPFM('simple_sphere_4.pfm')
I = g(data, gamma)*255.0
I = I.astype(np.uint8)
writePPM('simple_sphere_4.ppm', I)

data = loadPFM('simple_sphere_8.pfm')
I = g(data, gamma)*255.0
I = I.astype(np.uint8)
writePPM('simple_sphere_8.ppm', I)

data = loadPFM('simple_sphere_16.pfm')
I = g(data, gamma)*255.0
I = I.astype(np.uint8)
writePPM('simple_sphere_16.ppm', I)

data = loadPFM('simple_sphere_32.pfm')
I = g(data, gamma)*255.0
I = I.astype(np.uint8)
writePPM('simple_sphere_32.ppm', I)

data = loadPFM('simple_sphere_3232.pfm')
I = g(data, gamma)*255.0
I = I.astype(np.uint8)
writePPM('simple_sphere_3232.ppm', I)
