"""
元素操作
"""


def define_tuple():
    """
    定义一个元组
    :return:
    """
    return 1, 2, 3


def iterate(var: tuple):
    for _v in var:
        print("元组元素: " + str(_v))


if __name__ == '__main__':
    print(define_tuple())
    print(iterate(define_tuple()))
