import json


def main():
    my_dict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(my_dict, f)
    except IOError as e:
        print(e)
    print("save json data success")


if __name__ == '__main__':
    main()
