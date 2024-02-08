def greet_user(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)  


if __name__ == '__main__':
    usernames = ['hannah', 'ty', 'margot']
    greet_user(usernames)
    pass;   