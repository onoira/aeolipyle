"""Build scripts/download_workshop_items.steamcmd from boilerplate.steamcmd and fids"""
OUT = 'scripts/download_workshop_items.steamcmd'  # also as `$SCRIPT` in run.ps1

TMark = tuple[str, int]   # (mark, offset)
TIndex = tuple[int, int]  # (start, end)


class Config():

    MARK_LOGIN = ('//>login\n', 9)
    MARK_COMMAND = ('//>\n', 4)

    @staticmethod
    def get_appid() -> str:
        appid: str
        with open('settings/app.id', 'r', encoding='utf-8') as fp:
            appid = fp.readline().strip()
        return appid

    @staticmethod
    def get_username() -> str:
        username: str
        with open('settings/user.name', 'r', encoding='utf-8') as fp:
            username = fp.readline().strip()
        return username

    @staticmethod
    def get_fids() -> set[str]:
        fids = set()
        with open('fids', 'r', encoding='utf-8') as fp:
            for line in fp:
                fids.add(line.strip())
        return fids

    @staticmethod
    def get_boilerplate() -> str:
        boilerplate: str
        with open('scripts/boilerplate.steamcmd', 'r', encoding='utf-8') as fp:
            boilerplate = fp.read()
        return boilerplate


def get_indices(s: str, mark: TMark) -> TIndex:
    """Retrieve the start and end of a substring"""
    index_first = s.find(mark[0])
    return (index_first, index_first+mark[1])


def main() -> None:

    fids = Config.get_fids()
    appid = Config.get_appid()
    commands = str()
    for fid in fids:
        commands += f"workshop_download_item {appid} {fid}\n"

    boilerplate = Config.get_boilerplate()
    indices_lgn = get_indices(boilerplate, Config.MARK_LOGIN)
    indices_cmd = get_indices(boilerplate, Config.MARK_COMMAND)

    username = Config.get_username()
    script = boilerplate[:indices_lgn[0]] +\
        f"login {username}\n" +\
        boilerplate[indices_lgn[1]:indices_cmd[0]] +\
        commands +\
        boilerplate[indices_cmd[1]:]

    with open(OUT, 'w', encoding='utf-8') as fp:
        fp.write(script)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
