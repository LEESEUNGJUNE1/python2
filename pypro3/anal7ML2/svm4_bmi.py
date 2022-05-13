# BMI 식을 이용해 dataset을 작성 후 SVM 분류 모델 생성
# BMI 식 = 몸무게(kg) / (키(m)*키(m))
"""    - 데이터 활용을 위한 임의의 자료 만드는 방법 - 
print(69 / ((177 / 100) * (177 / 100)))

# BMI 식을 이용해 무작위 자료 작성
import random

def calc_func(h,w):
    bmi = w / (h / 100) ** 2
    if bmi < 18.5 : return 'thin'
    if bmi < 24.0 : return 'normal'
    return 'fat'

print(calc_func(171, 65))

fp = open('bmi.csv','w')
fp.write('height,weight,label\n')
cnt = {'thin':0,'normal':0,'fat':0}
random.seed(12)
for i in range(500000):
    h = random.randint(150, 200)
    w = random.randint(35, 100)
    label = calc_func(h, w)
    cnt[label] += 1
    fp.write('{0},{1},{2}\n'.format(h, w, label))
    
fp.close()
"""

# SVM 분류 모델을 적용
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tbl = pd.read_csv('bmi.csv')
print(tbl.head(3))

label = tbl['label']

# weight, height는 정규화 - 표준화나 정규화를 하면 성능이 좋아진다.
w = tbl['weight'] / 100
print(w[:3])
h = tbl['height'] / 200
print(h[:3])
wh= pd.concat([w, h], axis = 1)
print(wh.head(3),wh.shape)
print(label[:3],label.shape)
label = label.map({'thin':0,'normal':1,'fat':2}) # dummy (범주형 자료를 숫자값으로 할수있다.)
print(label[:3])

data_train, data_test, label_train, label_test = train_test_split(wh, label, random_state = 1)
print(data_train, data_test, label_train, label_test.shape)
print(data_train[:3])

# model = svm.SVC(C = 1).fit(data_train,label_train)
model = svm.LinearSVC(C = 1).fit(data_train,label_train)

pred = model.predict(data_test)
print('실제값 : ', label_test[:10].values)
print('예측값 : ', pred[:10])

print(metrics.accuracy_score(label_test, pred))
print(metrics.classification_report(label_test, pred))

tbl2 = pd.read_csv('bmi.csv', index_col = 2)
print(tbl2.head(2))
def scatter_func(lbl, color):
    b = tbl2.loc[lbl]
    plt.scatter(b['weight'], b['height'], c=color, label=lbl)

scatter_func('fat', 'red')
scatter_func('normal', 'yellow')
scatter_func('thin', 'blue')
plt.legend()
plt.show()