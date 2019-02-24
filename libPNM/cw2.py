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
    if depth < 1:
        if x.shape[0]>x.shape[1]:
            opt[yoffset+mh-1:yoffset+mh+1,xoffset:xoffset+x.shape[1]]=1
            cut(x[:mh,:], yoffset, xoffset, depth+1)
            cut(x[mh:,:], yoffset+mh, xoffset, depth+1)
        else:
            opt[yoffset:yoffset+x.shape[0],xoffset+mw-1:xoffset+mw+1]=1
            cut(x[:,:mw], yoffset, xoffset, depth+1)
            cut(x[:,mw:], yoffset, xoffset+mw, depth+1)
    else:
        opt[yoffset+mh-2:yoffset+mh+2, xoffset+mw-2:xoffset+mw+2, :2] = 0
        opt[yoffset+mh-2:yoffset+mh+2, xoffset+mw-2:xoffset+mw+2, 2] = 1
#load data
data = loadPFM('grace_latlong.pfm')
opt = data
data = np.mean(data, axis = 2)
scale = np.zeros(data.shape)
for i in range(512):
    scale[i,:] = np.sin(i/511.0*np.pi)
data = data * scale
cut(data, 0, 0, 0)
writePFM('./opt1.pfm', opt)
