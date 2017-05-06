# coding=utf-8
from __future__ import division
from matplotlib import pyplot as plt
import datetime,random,time
import numpy as np

print "---第二題---"
# lambda
circle=lambda r : 3.14*r*r

print(circle(5))

print "---第三題---"
# random不重複




print "---第四題---"
# matplotlib畫圖








print "---第五題---"
# 亂數矩陣相加




def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols
def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i, j) for j in range(num_cols)]
            for i in range(num_rows)]
def matrix_add(A, B):
    if shape(A) != shape(B):
        raise ArithmeticError("cannot add matrices with different shapes")
    num_rows, num_cols = shape(A)
    def entry_fn(i, j):
        return A[i][j] + B[i][j]
    return make_matrix(num_rows, num_cols, entry_fn)

print matrix_add(A,B)

print "---第六題---"
# 填空題
a1=0
a2=0
aboth=0
n=100000
def random_ball():
    return random.choice(["B", "Y"])
random.seed(2)
for _ in range(n):
    get1 = random_ball()
    get2 = random_ball()
    if get1 == "B":
        a1 += 1
    if get1 == "B" and get2 == "B":
        aboth += 1
    if get2 == "B":
        a2 += 1

print "P(aboth):",
print "P(get1): ",
print "P(get2): ",
print "P(get1,get2): ",
print "P(get1|get2) = p(aboth)/p(get2): ",
print "p(get1|get2)/p(get2) = p(get1)p(get2)/p((get2) = p(get1) : ",



