"""Parse urls and extract PublishedFileIds to fids file."""
FILE = 'urls'


class Fid():

    PARAM = ('?id=', 4)

    @classmethod
    def find(cls, url: str) -> str:
        return url[url.find(cls.PARAM[0])+cls.PARAM[1]:]


def main() -> None:

    urls: list[str] = []
    with open(FILE, 'r', encoding='utf-8') as fp:
        for l in fp:
            if not l.startswith('http'):
                continue
            urls.append(l.strip())

    fids: set[str] = set()
    for url in urls:
        fid: str = Fid.find(url)
        fids.add(fid+'\n')

    with open('fids', 'w', encoding='utf-8') as fp:
        fp.writelines(fids)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
