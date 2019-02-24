from PNM import *


#set gamma here
gamma = 2.2
n = 0


def half(x):
    s = np.cumsum(x)
    for i in range(s.shape[0]):
        if s[i]>np.sum(x)/2.0:
            return i
def cut(x, yoffset, xoffset, depth):
    global n
    global opt
    w = np.sum(x, axis = 0)
    h = np.sum(x, axis = 1)
    mw = half(w)
    mh = half(h)
    if depth < 6:
        if x.shape[0]>x.shape[1]:
            cut(x[:mh,:], yoffset, xoffset, depth+1)
            cut(x[mh:,:], yoffset+mh, xoffset, depth+1)
        else:
            cut(x[:,:mw], yoffset, xoffset, depth+1)
            cut(x[:,mw:], yoffset, xoffset+mw, depth+1)
    else:
        opt[yoffset:yoffset+x.shape[0], xoffset:xoffset+x.shape[1], :2] = 0
        opt[yoffset+mh-3:yoffset+mh+3, xoffset+mw-3:xoffset+mw+3, :2] = 0
        opt[yoffset+mh-3:yoffset+mh+3, xoffset+mw-3:xoffset+mw+3, 2] = 1
def g(x, gamma):
    x = x**(1/gamma)
    x[x>1] = 1.0
    return x
#load data
data = loadPFM('grace_latlong.pfm')
opt = data
print opt.shape
data = np.mean(data, axis = 2)
scale = np.zeros(data.shape)
for i in range(512):
    scale[i,:] = np.sin(i/511.0*np.pi)
data = data * scale
cut(data, 0, 0, 0)
I = g(opt, gamma)*255.0
I = I.astype(np.uint8)
writePFM('./opt62.pfm', opt)
writePPM('./opt62.ppm', I)
