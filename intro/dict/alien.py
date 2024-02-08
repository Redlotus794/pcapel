if __name__ == '__main__':
    # 使用字典
    alien_0 = {'color': 'green', 'points': 5}
    print(alien_0['color'])
    print(alien_0['points'])

    # 添加键值对
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    # 修改字典中的值
    alien_0['color'] = 'yellow'
    print("The alien is now " + alien_0['color'] + ".")

    # 删除键值对
    del alien_0['points']
    print(alien_0)

    # 由类似对象组成的字典
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    print("Sarah's favorite language is " +
          favorite_languages['sarah'].title() +
          ".")

    # 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
    person = {
        'first_name': 'zhang',
        'last_name': 'san',
        'age': 18,
        'city': 'beijing',
    }
    print(person['first_name'])
    print(person['last_name'])
    print(person['age'])
    print(person['city'])
