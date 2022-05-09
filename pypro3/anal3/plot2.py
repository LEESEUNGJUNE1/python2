import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)

"""
# 방법1 :  matplotlib style 의 인터페이스로 시각화 
plt.figure()
plt.subplot(2,1,1)  # row, column, panel number
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
plt.show()

# 방법2 : matplotlib의 객체지향 인터페이스로 시각화
fig, ax = plt.subplots(nrows =2, ncols=1)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
plt.show()
"""

"""
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.hist(np.random.randn(10), bins = 5, alpha = 0.9)   # bins = 구간 수 
ax2.plot(np.random.randn(10))
plt.show()
"""

data = [50, 80, 100, 70, 90]

plt.bar(range(len(data)), data)     # 세로막대
plt.show()

err = np.random.rand(len(data))     # 표준편차, 오차, 신뢰구간 등 표시 
plt.barh(range(len(data)), data, xerr=err, alpha = 0.5)    # 가로막대
plt.show()

plt.pie(data, explode=(0, 0.1, 0, 0, 0), colors=['yellow','red','blue'])
plt.title('pie chart')
plt.show()

plt.boxplot(data)
plt.show()

n = 30                              # 산포도 그래프 
np.random.seed(0)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.random.rand(n)
scale = np.pi * (15 * np.random.rand(n)) ** 2
plt.scatter(x, y, s = scale , c = color)
plt.show()

# 시계열 데이터
import pandas as pd
fdata = pd.DataFrame(np.random.randn(1000,4),
                     index=pd.date_range('1/1/2000', periods=1000),columns= list('abcd'))
print(fdata.head())

fdata = fdata.cumsum()  # 누적합
plt.plot(fdata)
plt.show()

# pandas 의 plot 기능
fdata.plot()
fdata.plot(kind='bar')
fdata.plot(kind='box')
plt.xlabel('time')
plt.ylabel('data')
plt.show()



