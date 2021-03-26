
from typing import Set, Tuple



# -- Retrieve list of PublishedFileIds

fids:Set[str] = set()
with open('fids', 'r', encoding='utf-8') as fp:
    for l in fp:
        fids.add(l.strip())


## -- Configuration -- ##

# -- Retrieve configured `app.id`

appid:str
with open('settings/app.id', 'r') as fp:
    appid = fp.readline().strip()

# -- Retrieve configured `user.name`

username:str
with open('settings/user.name', 'r') as fp:
    username = fp.readline().strip()


## -- Script -- ##

def get_indices(s:str, mark:str) -> Tuple[int]:
    index_first = s.find(mark[0])
    return (index_first, index_first+mark[1])

# -- Generate command block

_script = str()
for fid in fids:
    _script += f"workshop_download_item {appid} {fid}\n"

# -- Retrieve boilerplate

boilerplate:str
with open('scripts/boilerplate.txt', 'r') as fp:
    boilerplate = fp.read()

# -- Get substring indices (login)

MARK_LOGIN = ('//>login\n', 9)
indices_lgn:Tuple[int, int] = get_indices(boilerplate, MARK_LOGIN)

# -- Get substring indices (command)

MARK_COMMAND = ('//>\n', 4)
indices_cmd:Tuple[int, int] = get_indices(boilerplate, MARK_COMMAND)

# -- Generate script

script = boilerplate[:indices_lgn[0]]               +\
         f"login {username}\n"                      +\
         boilerplate[indices_lgn[1]:indices_cmd[0]] +\
         _script                                    +\
         boilerplate[indices_cmd[1]:]

with open('scripts/download_workshop_items.txt', 'w', encoding='utf-8') as fp:
    fp.write(script)
