# Aggrate-Demand
It is basic model for macro economic Aggrate Deman. 
import numpy as np
import matplotlib.pyplot as plt
Y = np.random.randint(0,100,10)
c0 = 10
C = []
for c in np.random.randint(0,10):
      Sonuc   = c0+c*Y 
      C.append(Sonuc)
      
i= np.random.randint(0,10)
I = i*Y
G= 50
AD = []
GDP = C+I+G
AD.append(GDP)
AS= []
AS.append(Y)
plot.plt(AD,AS)
plt.show()
