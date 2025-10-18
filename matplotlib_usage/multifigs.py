import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

fig1 = plt.figure()
ax1 = fig1.add_subplot(2,1,1)
ax1.plot(x, np.sin(x), label='sin(x)')
plt.legend(loc='upper right',title='Title')
ax2 = fig1.add_subplot(2,1,2)
ax2.plot(x, np.cos(x), label='cos(x)')
plt.legend(loc='upper right',title='Title')
plt.savefig('./output_image/multifigs.jpg',dpi=200)
plt.show()