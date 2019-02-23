from PNM import *


#set gamma here
gamma = 2.2

def half(x):
    s = np.cumsum(x)
    for i in range(s.shape[0]):
        if s[i]>np.sum(x)/2.0:
            return i
def cut(x, yoffset, xoffset, depth, opt):
    if x.shape[0]>x.shape[1]:
        s = np.sum(x, axis = 1)
        middle = half(s)        
        opt[yoffset+middle,xoffset:xoffset+s.shape[0]]=1
        if depth != 0:
            cut(x[:middle,:], yoffset, xoffset, depth-1, opt)
            cut(x[middle:,:], yoffset+middle, xoffset, depth-1, opt)
    else:
        s = np.sum(x, axis = 0)
        middle = half(s)
        opt[yoffset:yoffset+s.shape[0],xoffset+middle]=1
        if depth != 0:
            cut(x[:,:middle], yoffset, xoffset, depth-1, opt)
            cut(x[:,middle:], yoffset, xoffset+middle, depth-1, opt)


#load data
data = loadPFM('grace_latlong.pfm')
opt = data
data = np.mean(data, axis = 2)
scale = np.zeros(data.shape)
for i in range(512):
   scale[i,:] = np.sin(i/511.0*np.pi)
data = data * scale
cut(data, 0, 0, 1, opt)
writePFM('./opt.pfm', opt)
