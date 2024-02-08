"""
这是一个关于string操作实例的python文件
"""


def remove_right_blank(s):
    """
    移除右空白字符串函数
    :param s:
    :return:
    """
    print("移除右空白: " + s.rstrip())


def remove_left_blank(s):
    """
    移除左空白字符串的函数
    :param s:
    :return:
    """
    print("移除左空白: " + s.lstrip())



if __name__ == '__main__':
    remove_left_blank('  python')
    remove_right_blank('python ')
