if __name__ == '__main__':
    # 定义三个外星人列表
    aliens = []
    # 创建30个绿色的外星人
    for alien_number in range(30):
        new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        aliens.append(new_alien)
    # 显示前五个外星人
    for alien in aliens[:5]:
        print(alien)
    print("...")
    # 显示创建了多少个外星人
    print("Total number of aliens: " + str(len(aliens)))
    # 修改前三个外星人的属性
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['points'] = 10
            alien['speed'] = 'medium'
    
    # 6.4.2 
    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    # 概述所点的比萨
    print("You ordered a " + pizza['crust'] + "-crust pizza " +
          "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)


    # 6.4.3 在字典中存储字典
    users = {
        'aeinstein': { 
            'first': 'albert', 
            'last': 'einstein', 
            'location': 'princeton',
        },
        'mcurie': { 
            'first': 'marie', 
            'last': 'curie', 
            'location': 'paris',
        },
    }

    for username, user_info in users.items():
        print("\nUsername: " + username)
        full_name = user_info['first'] + " " + user_info['last']
        location = user_info['location']
        print("\tFull name: " + full_name.title())
        print("\tLocation: " + location.title())

        

    