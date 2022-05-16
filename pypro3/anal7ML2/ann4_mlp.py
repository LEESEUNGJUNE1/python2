# MLP : 다층신경망 - 선형 / 비선형 예측 모델 가능

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1]) # and
#label = np.array([0,1,1,1]) # or
label = np.array([0,1,1,0]) # xor - 하나의 노드만으로는 정확도가 0.5밖에 나오지 않는다.

# ml = MLPClassifier(hidden_layer_sizes=10, activation='relu',
#                    solver='adam', learning_rate_init = 0.01).fit(feature, label) # learning_rate_init 학습율 얼마만큼 이동할것이다.
ml = MLPClassifier(hidden_layer_sizes=(10, 10, 10), activation='relu',
                   solver='adam', learning_rate_init = 0.01).fit(feature, label)

print(ml)

pred = ml.predict(feature)
print('pred : ', pred)
print('acc : ', accuracy_score(label, pred))
