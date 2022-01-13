from xstavka_parse_package.parse import parse_list

if __name__ == '__main__':
    url_list = [
        r'https://1xstavka.ru/line/Volleyball/',
        # r'https://1xstavka.ru/line/Football/',
        # r'https://1xstavka.ru/line/Tennis/',
        # r'https://1xstavka.ru/line/Ice-Hockey/',
    ]

    parse_list(url_list)
