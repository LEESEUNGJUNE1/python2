# 인공신경망 : 단층 신경망(뉴런 또는 노드 1개) - Perceptron
# input data * 가중치의 합에 대해 임계값(활성화 함수)을 이항 분류가 가능

import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
# label = np.array([0,0,0,1]) # and
# label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor - 하나의 노드만으로는 정확도가 0.5밖에 나오지 않는다.


ml = Perceptron(max_iter=10, eta0=0.1).fit(feature, label) # 학습횟수,학습율
print(ml)
pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))