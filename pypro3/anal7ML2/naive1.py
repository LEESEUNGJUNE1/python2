# 나이브 베이즈 (Naive Bayes) 모델 : 베이지 정리를 이용
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder

x = np.array([1,2,3,4,5])
x = x[:, np.newaxis] # 2차원으로 설정
print(x)
y = np.array([1,3,5,7,9])

model = GaussianNB().fit(x,y)
print(model)
pred = model.predict(x)
print(pred)
print('acc : ',metrics.accuracy_score(y, pred))

# 새로운 값으로 분류
new_x = np.array([[0.5],[2],[7],[12],[0.1]])
new_pred = model.predict(new_x)
print('new_pred : ',new_pred)

print('--- One-hot encoding ---')
# 1. np.eye()
x = '1,2,3,4,5'
x = x.split(',')
x = np.eye(len(x))
print(x)

# 2. OneHotEncoder 사용
x = '1,2,3,4,5'
x = x.split(',')
x = np.array(x)
x = x[:, np.newaxis]
one_hot = OneHotEncoder(categories = 'auto')
x2 = one_hot.fit_transform(x).toarray()
print(x2)
y = np.array([1,3,5,7,9])

model2 = GaussianNB().fit(x2,y)
print(model2)
pred2 = model.predict(x2)
print(pred2)



