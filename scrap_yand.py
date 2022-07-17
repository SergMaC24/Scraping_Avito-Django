import json

from fake_useragent import UserAgent
import requests

ua = UserAgent()


def items_data():
    response = requests.get(
        url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=35&isStore=true&limit=60&maxPrice=67.79444304543078&minPrice=16.948610761357696&offset=420&sort=botFirst&type=5&type=3&withStack=true',
        headers={'user-agent': f'{ua.random}'}
    )

    # with open('result.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    b_size = 60

    while True:
        for item in range(offset, offset + b_size, 60):
            url = item
            print(url)
            offset += b_size


def main():
    items_data()


if __name__ == '__main__':
    main()