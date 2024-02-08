if __name__ == '__main__':
    """
    字符串拼接
    """
    age = 23
    # message = "Happy " + age + "rd Birthday!"
    # print(message)  # 会报错

    # it's ok
    message = "Happy " + str(age) + "rd Birthday!"
    print(message)