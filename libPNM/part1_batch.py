from PNM import *

#try different combinations of gamma and stops
stops_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gamma_list = [1.0, 1.5, 1.8, 2.2, 2.5, 3.0]

#load data
Z1 = loadPFM('./../Office/Office1.pfm')
Z2 = loadPFM('./../Office/Office2.pfm')
Z3 = loadPFM('./../Office/Office3.pfm')
Z4 = loadPFM('./../Office/Office4.pfm')
Z5 = loadPFM('./../Office/Office5.pfm')
Z6 = loadPFM('./../Office/Office6.pfm')
Z7 = loadPFM('./../Office/Office7.pfm')

#concatenate data
Zlist = [Z1, Z2, Z3, Z4, Z5, Z6, Z7]
Dt = 1
lg = []
weighted_list = []

#weighted function
def w(x):
   return (1-np.cos(np.pi*2*x))/2
#function implementing gamma and +stops
def g(x, n, gamma):
   return (x*(2**n))**(1/gamma)

#for all images
for Zi in Zlist:
   #set to 1 to discard these values (their weight = 0)
   Zi[np.logical_or(Zi < 0.005, Zi > 0.92)] = 1
   #follows the algorithm given in the spec
   Ei = Zi/Dt
   weighted_exposure = w(Zi)
   weighted_list.append(weighted_exposure)
   a = np.log(Ei)
   lg.append(a*weighted_exposure)
   Dt = Dt * (2 ** 2)

sum_values = sum(lg)
sum_exposure = sum(weighted_list)

#We have the initial F(x,y) here
F = np.exp(sum_values/sum_exposure)

#stops, gamma, converting to ppm, saving image, etc.
for gamma in gamma_list:
   for stops in stops_list:
      F_modify = g(F, stops, gamma)
      F_modify[F_modify>1] = 1
      I = F_modify*255.0
      I = I.astype(np.uint8)
      writePPM('./../output/%.1fg_%is.ppm' %(gamma,stops), I)
      writePFM('./../output/%.1fg_%i.pfm' %(gamma,stops), F_modify)



