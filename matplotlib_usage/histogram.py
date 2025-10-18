import matplotlib.pyplot as plt
import numpy as np

mu ,sigma = 100,20

x=mu+sigma*np.random.randn(100000)

plt.hist(x,bins=50)
plt.xlabel("IQ")
plt.ylabel("Frequency")
plt.title("Histogram of IQ values")
plt.grid(True)
plt.show()