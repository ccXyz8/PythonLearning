import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc("font", family="YouYuan")
x = np.linspace(0,5,100)

plt.axis([0,5,0,100])
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.title('标题')

plt.plot(x,x**2,label='x^2')
plt.plot(x,x**3,label='x^3')
plt.legend(loc='upper right',title="标题")

for _ in range(2):
    plt.savefig(f'./output_image/image{_}.jpg',dpi=200)    #png格式的也行

plt.show()



