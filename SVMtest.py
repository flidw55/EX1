from sklearn import datasets
from sklearn import svm
import matplotlib.pyplot as plot

clf = svm.SVC(gamma=0.001, C=100.)
iris = datasets.load_iris()
clf.fit(iris.data[:-10], iris.target[:-10])
result=clf.predict(iris.data[:-10])

print ("predict")
print clf
print("real")
print(iris.data[-10:])
print (iris.target[-10:])

print("----------------")

TestSeven={'images':[[0.00 ,0.00 ,4.00 ,6.00 ,6.00 ,4.00 ,0.00 ,0.00],
[0.00 ,0.00 ,16.00 ,16.00 ,16.00 ,16.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,0.00 ,0.00 ,16.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,0.00 ,16.00 ,4.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,16.00 ,5.00 ,0.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,16.00 ,3.00 ,0.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,9.00 ,2.00 ,0.00 ,0.00 ,0.00],
[0.00 ,0.00 ,0.00 ,0.00 ,0.00 ,0.00 ,0.00 ,0.00]]

,'data':[0.00 ,0.00 ,4.00 ,6.00 ,6.00 ,4.00 ,0.00
        ,0.00,0.00 ,0.00 ,16.00 ,16.00 ,16.00 ,16.00
        ,0.00 ,0.00,0.00 ,0.00 ,0.00 ,0.00 ,0.00 ,16.00
        ,0.00 ,0.00,0.00 ,0.00 ,0.00 ,0.00 ,16.00 ,4.00
        ,0.00 ,0.00,0.00 ,0.00 ,0.00 ,16.00 ,5.00 ,0.00 ,0.00
        ,0.00,0.00 ,0.00 ,0.00 ,16.00 ,3.00 ,0.00 ,0.00 ,0.00,0.00
        ,0.00 ,0.00 ,9.00 ,2.00 ,0.00 ,0.00 ,0.00,0.00 ,0.00 ,0.00 ,0.00
        ,0.00 ,0.00 ,0.00 ,0.00]} #7


clf = svm.SVC(gamma=0.001, C=100.)
digits = datasets.load_digits()
clf.fit(digits.data[:-1], digits.target[:-1])
result=clf.predict(TestSeven['data'])

print(digits)
print(digits.data[-1])
print(digits.images[-1])
print("predict")
print result
print("real=7")
plot.figure(1, figsize=(3, 3))
plot.imshow(TestSeven['images'], cmap=plot.cm.gray_r, interpolation='nearest')
plot.show()
