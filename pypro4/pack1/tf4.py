# 연산자, 함수

# add, subtract, multiply, divide
# 삼항연산

import numpy as np
import tensorflow as tf

f1 = lambda : tf.constant(1) # 람다 객채의 주소
print(f1())

f2 = lambda : tf.constant(2)
a = tf.constant(3)
b = tf.constant(4)

# case 조건
result = tf.case([(tf.less(a,b), f1)],default = f2) # =if(a<b)return1 else return2
print(result.numpy())

# 관계 / 논리 연산
print()
print(tf.equal(1,2).numpy()) # 같다.
print(tf.not_equal(1,2)) # 같지않다.
print(tf.less(1,2)) # 작다.
print(tf.greater(1,2)) # 크다.
print(tf.greater_equal(1,2)) # 크거나 같다.

print(tf.logical_and(True, False).numpy())
print(tf.logical_or(True, False).numpy())
print(tf.logical_not(True, False).numpy())

#tf.reduce...
ar = [[1, 2], [3, 4]]
print(tf.reduce_sum(ar)) # 합
print(tf.reduce_mean(ar)) # 전체평균
print(tf.reduce_mean(ar, axis = 0)) # 열기준 평균
print(tf.reduce_mean(ar, axis = 1)) # 행기준 평균