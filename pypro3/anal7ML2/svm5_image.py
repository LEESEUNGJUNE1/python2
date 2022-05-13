# SVM으로 이미지 분류
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from pipes import makepipeline

faces = fetch_lfw_people(min_faces_per_person = 60, color = False)
print(faces)
# print(faces.DESCR)

print(faces.data)
print(faces.data.shape) # (1348, 2914)
print(faces.target) # [1 3 3 ... 7 3 5]
print(faces.target_names) # ['Ariel Sharon' 'Colin Powell' 'Donald Rumsfeld' 'George W Bush' ...
print(faces.images.shape) # (1348, 62, 47) 62행 47열 의 이미지가 1348개 있다.

# 이미지 한장 보기
# print(faces.images[1])
# print(faces.target_names[faces.target[1]])
# plt.imshow(faces.images[1], cmap='bone')
# plt.show()

fig,ax = plt.subplots(3,5) # 해상도 구하기
# print(fig) # Figure(640x480)
# print(ax.flat)
# print(len(ax.flat))
# 여러개의 이미지 보기
# for i, axi in enumerate(ax.flat):
#     axi.imshow(faces.images[i], cmap='bone')
#     axi.set(xticks = [], yticks = [], xlabel = faces.target_names[faces.target[i]])
# plt.show()

# PCA로 이미지 차원을 축소한 후 분류 모델 작성
m_pca = PCA(n_components = 150, whiten = True, random_state = 0) # 이미지에 가장 큰영향을 주는 150의 주성분. 차원축소된 데이터로 추출
x_row = m_pca.fit_transform(faces.data) # 1차원 근사값을 반환
print('x_row : ', x_row, x_row.shape) # (1348, 150)

# PCA가 선행된 데이터로 SVM 모델 작성
m_svc = SVC(C = 1) # 가중치를 규제
model = make_pipeline(m_pca, m_svc)
print(model)

# train / test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, random_state = 1)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape) # (1011, 2914) (337, 2914) (1011,) (337,)
print(x_train[0])
print(y_train[0])

model.fit(x_train, y_train)
pred = model.predict(x_test)
print('pred : ', pred[:10])
print('real : ', y_test[:10])

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
mat = confusion_matrix(y_test, pred)
print('confusion matrix : \n', mat)
print('accuracy : ', accuracy_score(y_test,pred)) # 0.7952
print('classification_report : ', classification_report(y_test, pred, target_names = faces.target_names))

# 분류 결과 시각화
fig,ax = plt.subplots(4,6)

for i, axi in enumerate(ax.flat):
    axi.imshow(x_test[i].reshape(62, 47), cmap='bone')
    axi.set(xticks = [], yticks = [])
    axi.set_ylabel(faces.target_names[pred[i]].split()[-1], color = 'black' if pred[i] == y_test[i] else 'red')
plt.show()

# 오차 행렬 시각화
import seaborn as sns
sns.heatmap(mat.T, square = True, annot = True, fmt = 'd', cbar = False,
            xticklabels = faces.target_names, yticklabels = faces.target_names)
plt.xlabel('real label')
plt.ylabel('predict label')
plt.show()