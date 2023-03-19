"""Reverse fids to URLs"""
BASEURL = 'https://steamcommunity.com/sharedfiles/filedetails/?id='


def main() -> None:
    with open('fids', 'r', encoding='utf-8') as fp:
        for line in fp:
            print(BASEURL+line.strip())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
