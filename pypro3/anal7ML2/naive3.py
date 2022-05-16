# weather dataset으로 비 유무 처리용 나이브베이즈 분류 모델 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import metrics

df = pd.read_csv("../testdata/weather.csv")
print(df.head(3))
print(df.info())

x = df[['MinTemp', 'MaxTemp', 'Rainfall']]
label = df['RainTomorrow'].map({'Yes':1, 'No':0})
print(x[:3])
print(label[:3])

# train / test 
train_x, test_x, train_y, test_y = train_test_split(x, label, random_state = 0)

gmodel = GaussianNB()
gmodel.fit(train_x,train_y)

pred = gmodel.predict(test_x)
print('예측값 :', pred[:10])
print('실제값 :', test_y[:10].values)

print('acc : ', accuracy_score(test_y, pred))
print('report : \n', metrics.classification_report(test_y, pred))