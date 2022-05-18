# 선형회귀 분석 선행 실습
# cost를 최소화 하는 과정을 시각화

import tensorflow as tf
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
# y = [1,2,3,4,5]
y = [2,4,6,8,10]
b = 0

#hypothesis = x * w + b (선형회귀 공식)
#cost = tf.reduce_sum(tf.pow(hypothesis - y,2)) / len(x)

w_val = [] # w 값의 변수
cost_val = [] #cost 값의 변수
for i in range(-30, 50):
    feed_w = i * 0.1 # (w값 * 학습율)
    #print(feed_w)
    hypothesis = tf.multiply(feed_w, x) + b # y = wx+b
    cost = tf.reduce_mean(tf.square(hypothesis - y))
    cost_val.append(cost)
    w_val.append(feed_w)
    print(str(i) + '' + ', cost : ' + str(cost.numpy()) + ', weight : ' + str(feed_w))

plt.scatter(w_val, cost_val)
plt.xlabel('weight')
plt.ylabel('cost')
plt.show()