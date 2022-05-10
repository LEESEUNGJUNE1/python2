# ROC curve : ROC(Receiver Operating Characteristic) curve는
# 다양한 threshold에 대한 이진분류기의 성능을 한번에 표시한 것이다.
# 이진 분류의 성능은 True Positive Rate와 False Positive Rate 두 가지를 이용해서 표현하게 된다.
# ROC curve를 한 마디로 이야기하자면 ROC 커브는 좌상단에 붙어있는 커브가 더 좋은 분류기를 의미한다고 생각할 수 있다.

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

# 분류 연습용 샘플 데이터 작성
x, y = make_classification(100, n_features = 2, n_redundant = 0, random_state = 123) # 표본, 독립변수
print(x[:3])
print(y[:3])

# import matplotlib.pyplot as plt
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

model = LogisticRegression().fit(x,y)
y_hat = model.predict(x) # 예측값 : x값으로 예측하겠다.
print('y_hat : ', y_hat[:3])

print()
f_value = model.decision_function(x) # 결정함수(판별함수) : 불확실성 추정함수 - 판별 경계선 설정을 위함
print('f_value : ', f_value[:10])
df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns = ['f','y_hat','y'])
print(df.head(3))

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat))
acc = (44 + 44) / 100 # (TP + TN) /전체수 <-정확도
recall = 44 / (44 + 4) # TP / TP + FN <-재현도,민감도
specificity = 44 / (8 + 44) # TN / FP + TN <-특이도
fallout = 8 / ( 8 + 44 ) # FP / (FP + TN) # 위양성율

print('acc(정확도) : ', acc)
print('recall(재현도,민감도) : ', recall) # TPR : 전체 양성 샘플 중에 양성으로 예측된 것의 비율
print('specificity(특이도) : ', specificity)
print('fallout(위양성율) : ', fallout) # FPR(1-특이도) : 전체 음성 샘플 중에 양성으로 잘못 예측된것의 비율
# TPR은 1에 가까울수록 좋다 / FPR은 0에 가까울수록 좋다.

print()
from sklearn import metrics
ac_sco = metrics.accuracy_score(y, y_hat)
print('ac_sco : ', ac_sco)
cl_rep = metrics.classification_report(y, y_hat)
print('cl_rep : ', cl_rep)

print()
fpr, tpr, thresholds = metrics.roc_curve(y,model.decision_function(x)) # 실제값, 판별함수값
print('fpr : ',fpr)
print('tpr : ',tpr)
print('분류 결정 임계값 thresholds : ',thresholds)

# ROC curve 시각화
import matplotlib.pyplot as plt
plt.plot(fpr, tpr, 'o-', label = 'LogisticRegression')
plt.plot([0, 1],[0, 1], 'k--', label = 'random classifier line(AUC:0.5')
plt.plot([fallout], [recall], 'r+', ms = 20)
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.title('ROC curve')
plt.legend()
plt.show()

# AUC (Area Under the ROC Curve)는 ROC curve의 밑면적을 말한다.
# 즉, 성능 평가에 있어서 수치적인 기준이 될 수 있는 값으로, 1에 가까울수록 그래프가 좌상단에 근접하게 되므로 좋은 모델이라고 할 수 있다.
print('AUC : ', metrics.auc(fpr, tpr))

# 해석 : ...