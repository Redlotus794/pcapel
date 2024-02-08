if __name__ == '__main__':
    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi'
    }

    for key, value in user_0.items():
        print("\nKey: " + key)
        print("Value: " + value)

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }

    for name, language in favorite_languages.items():
        print(name.title() + "'s favorite language is " +
              language.title() + ".")
        
    # 遍历字典中的所有键
    for name in favorite_languages.keys():
        print(name.title())

    # 遍历字典中的所有值
    for language in favorite_languages.values():
        print(language.title())
    
    # 按顺序遍历字典中的所有键
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll.")

    # 遍历字典中的所有值
    print("The following languages have been mentioned:")
    for language in set(favorite_languages.values()):
        print(language.title())
    
    
