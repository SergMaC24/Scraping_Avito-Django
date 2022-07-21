import json

from fake_useragent import UserAgent
import requests

ua = UserAgent()


def items_data():
    # response = requests.get(
    #     url='https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=35&isStore=true&limit=60&maxPrice=67.79444304543078&minPrice=16.948610761357696&offset=420&sort=botFirst&type=5&type=3&withStack=true',
    #     headers={'user-agent': f'{ua.random}'}
    # )

    # with open('result.json', 'w') as file:
    #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

    offset = 0
    b_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + b_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=35&isStore=true&limit=60&maxPrice=5000&minPrice=1000&offset={item}&sort=botFirst&type=5&type=3&withStack=true'
            response = requests.get(
                url=url,
                headers={'user-agent': f'{ua.random}'}
            )
            offset += b_size

            data = response.json()
            items = data.get('items')

            for i in items:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullName')
                    item_3d = i.get('3d')
                    item_img = i.get('img')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')
                    item_pattern = i.get('pattern')

                    result.append(
                        {
                            'name': item_full_name,
                            '3d': item_3d,
                            'img': item_img,
                            'price': item_price,
                            'overprice': item_over_price,
                            'pattern': item_pattern
                        }
                    )

        count += 1
        print(f'Page{count}')
        print(url)

        if len(items) < 60:
            break

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))


def main():
    items_data()


if __name__ == '__main__':
    main()