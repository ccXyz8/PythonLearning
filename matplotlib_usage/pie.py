import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']

labels = ['住房','餐饮','娱乐','其他']
percentages =[60.2,20.5,15.1,4.2]
plt.pie(percentages,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('支出占比')
plt.show()

explode = (0.1,0,0,0)
plt.pie(percentages,labels=labels,explode=explode,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('支出占比')
plt.show()
