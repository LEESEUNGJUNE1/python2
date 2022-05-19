# 자동차 관련 데이터로 선형회귀모델 작성
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from keras import layers
from keras.losses import mean_absolute_error

dataset = pd.read_csv("../testdata/auto-mpg.csv")
print(dataset.head(2))
del dataset['car name'] # 연관성이 아예없는 차 이름부터 삭제
print(dataset.columns)
print(dataset.corr())
dataset.drop(['acceleration','model year','origin'], axis='columns', inplace = True)
# print(dataset.info())

dataset['horsepower'] = dataset['horsepower'].apply(pd.to_numeric, errors='coerce') # 강제 형변환시 에러가 발생함으로 errors='coerce' 쓰면 에러를 무시할수있다.
# print(dataset.info())
print(dataset.isna().sum())
dataset = dataset.dropna()
print(dataset.info())

print(dataset.head(2))

# sns.pairplot(dataset[['mpg','cylinders','displacement','horsepower','weight']])
# plt.show()

# train/test split : sample() 함수
train_data = dataset.sample(frac = 0.7, random_state = 123)
test_data = dataset.drop(train_data.index)
print(train_data[:2],'', train_data.shape)  # (274, 5)
print(test_data[:2],'', test_data.shape)    # (118, 5)

print('--- train data 표준화 선행 작업 ---')
# train data 표준화 선행 작업
train_stat = train_data.describe()
train_stat.pop('mpg')
train_stat = train_stat.transpose()
print(train_stat)

# label : mpg(연비)
train_label = train_data.pop('mpg')
test_label = test_data.pop('mpg')
print(train_label[:2])
print(test_label[:2])

# feature에 대해서 표준화 진행
# print(train_data[:2])
def st_func(x): # (요소값 - 평균) / 표준편차
    return(x-train_stat['mean'])/train_stat['std']

# print(st_func(10))
# print(st_func(train_data[:2]))
st_train_data = st_func(train_data)
st_test_data = st_func(test_data)

print(st_train_data[:3])
print(train_label[:3])

print('--------------------')
from keras.models import Sequential
from keras.layers import Dense

def build_model():
    network = Sequential([
        Dense(units=64, activation=tf.nn.relu, input_shape = [4]),
        Dense(units=64, activation=tf.nn.relu),
        Dense(units=1, activation='linear'),
    ])
    # opti = tf.keras.optimizers.RMSprop(0.001)
    opti = tf.keras.optimizers.Adam(0.01)
    network.compile(optimizer=opti, loss='mean_squared_error',
                    metrics=['mean_absolute_error','mean_squared_error'])   # mae, mse
    return network
    
model = build_model()
print(model.summary())    

# fit 전에 predict() 가능 : 결과는 기대하지 말자

epochs = 5000 # 일부러 많이 학습하게 설정해둔다.

early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', mode = 'auto', patience=5)

history = model.fit(st_train_data, train_label, batch_size = 32, epochs=epochs,
                    validation_split=0.2, verbose=1, callbacks=[early_stop])
df = pd.DataFrame(history.history)
print(df.columns)
print(df.head(2))

# 모델의 성능(mae, mse) 시각화 - (성능확인) 오차값을 확인할때 사용 mse가 좀더 확실하게 눈으로 볼수있다.
def plot_history(history):
    hist = pd.DataFrame(history.history)
    hist['epoch'] = history.epoch
    plt.figure(figsize=(8,12))

    plt.subplot(2,1,1)
    plt.xlabel('epochs')
    plt.ylabel('mae[MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'], label = 'train err')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label = 'val err')
    plt.legend()

    plt.subplot(2,1,2)
    plt.xlabel('epochs')
    plt.ylabel('mae[$MPG^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'], label = 'train err')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'], label = 'val err')
    plt.legend()

    plt.show()

plot_history(history)