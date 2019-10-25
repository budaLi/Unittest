from itertools import chain

mylist = [1, 2, 3]
mydic = {
    "id": 1,
    "name": 2
}


# chain函数可以将多个可迭代的对象进行组合
# for value in chain(mydic, mydic, range(5, 10)):
#     print(value)


# 自己实现的chain函数
def my_chain(*args, **kwargs):
    for iterable in args:
        yield from iterable

        # for value in iterable:
        #     yield value


for value in my_chain(mylist, mydic):
    print(value)
