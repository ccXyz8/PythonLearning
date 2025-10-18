import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

x = [1,2,3,4,5]
y = [5,7,4,3,8]

colors = ['red','green','black','orchid','blue']
x_label = ['华中','华南','华东','华北','华西']
plt.xticks(x,x_label)
plt.bar(x,y,color=colors)
plt.xlabel('地区')
plt.ylabel('销售额（单位：百万）')
plt.title('各地区年度销售额')
plt.grid(True,linestyle=':',color='0.75',alpha=0.5)
plt.show()

#横着
y = [1,2,3,4,5]
x = [5,7,4,3,8]

y_label = ['华中','华南','华东','华北','华西']
plt.yticks(y,y_label)
plt.barh(y,x,color=colors)
plt.ylabel('地区')
plt.xlabel('销售额（单位：百万）')
plt.grid(True,linestyle=':',color='0.75',alpha=0.5)
plt.show()

