import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)
y = np.random.randn(1000)

size = np.random.randn(1000)
colors = np.random.rand(1000)

plt.scatter(x,y,c=colors,s=size)
plt.show()