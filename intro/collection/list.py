"""
这是一个关于list对象的python文件
"""


def list_define() -> list:
    """
    list定义
    :return:
    """
    bicycles = ['trek', 'cannodale', 'redline', 'specialized']
    return bicycles


def random_access(var: list, pos: int):
    """
    随机访问
    :param pos: 随机访问位置
    :param var: list
    :return:
    """
    print("随机访问索引为" + str(pos) + "的元素: ", var[pos])


def append_element(var: list, elem: object) -> list:
    """
    添加元素
    :param var:
    :param elem:
    :return:
    """
    var.append(elem)
    return var


def insert_element(var: list, pos: int, elem: object) -> list:
    """
    list中特定位置插入某个元素
    :param var:
    :param pos:
    :return:
    """
    var.insert(pos, elem)
    return var


def copy_list(var: list):
    """
    复制列表
    :param var:
    :return:
    """
    return var[:]


if __name__ == '__main__':
    """
    关于list
    """
    print(list_define())
    random_access(list_define(), 2)
    random_access(list_define(), -1)  # 最后一个元素
    print(append_element(list_define(), 'abc'))  # 添加元素
    print(insert_element(list_define(), 2, 'abc'))
    print(copy_list(list_define()))

