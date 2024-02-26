import math
T=0

#svpc : slope vapor pressure curve (kPa/°C)
svpc= 4098*(4.584*math.exp(17.27*T/237.3+T))/(T+237.3)**2
svpc=svpc*0.133322

#u : wind speed (ms-1)
u=0
