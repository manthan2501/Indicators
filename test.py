import numpy as np
import matplotlib.pyplot as plt
from Averages import Dynamic_SMA
from RSI_dynamic import RSI_Dynamic

s=[500]
ma=[0]
rsi=[]
sma=Dynamic_SMA(8)
ind=RSI_Dynamic(8,5)
for i in range(500):
    s.append(s[-1]+2*np.random.normal(8,8)*(2*np.random.randint(2)-1))
    ma.append(sma.update_and_get(s[-1]))
    rsi.append(ind.update_and_get(s[-1]))
plt.plot(s)
plt.plot(ma)
plt.show()
plt.plot(rsi)
print(rsi)
plt.show()

