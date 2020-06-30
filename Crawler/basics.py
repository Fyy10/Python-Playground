# from functools import reduce
from flask import Flask
app = Flask(__name__)


# homemade reduce function
def reduce(f, it):
    for i in range(len(it)):
        if i == 0:
            ans = it[i]
        else:
            ans = f(ans, it[i])
    return ans


def test_args(*args):
    print(type(args))
    for arg in args:
        print(arg)


def test_kwargs(**kwargs):
    print(type(kwargs))
    for kw in kwargs:
        print(kw)
    print(kwargs)


def test_map(item):
    return item * 2


# add function for reduce
def add(x, y):
    return x + y


# [show(i) for i in range(10) if i > 2]
def show(x):
    print(x, end=' ')


# flask
@app.route("/")
def hello():
    return "Hello World!"


# class
class Crawler(object):
    # 类属性
    name = "Crawl"

    # 构造函数
    def __init__(self, name):
        # 实例属性
        self.name = name
        # 带_的实例属性不会自动显示（私有）
        self._hide = 'a'

    # 实例函数，self表示当前实例
    def show(self):
        print(self.name)

    # 定义静态函数
    @staticmethod
    def show1():
        print(Crawler.name)


# functions
test_args(1, 2, 3)
test_kwargs(a=1, b=2, c=3)

# map
a = list(range(10))
# function, iterable
data = list(map(test_map, a))
print(data)

# map - list
tmp_list = []
for item in a:
    tmp_list.append(test_map(item))
print(tmp_list)


# reduce
data = list(map(test_map, range(10)))
data = reduce(add, data)
print(data)

# lambda
print(type(lambda x: x+1))

# filter
data = range(10)
data = filter(lambda data_it: data_it > 5, data)
print(list(data))

# 切片（前闭后开）
# [开始:结束:步长]
a = list(range(10))
print(a[2:9])
print(a[2:8:2])

# list
[show(i) for i in range(10)]
print()

# class
c = Crawler('haha')
print(Crawler.name)
print(c.name)
c.show()
c.show1()

# flask
app.run()
