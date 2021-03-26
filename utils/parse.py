
from typing import List, Set



# -- Find all URLs (starting with 'HTTP')
urls:List[str] = list()
with open('urls.txt', 'r') as fp:
    for l in fp:
        if not l.startswith('http'):  continue
        urls.append(l.strip())

# -- Retrieve PublishedFileIds

PARAM  = ('?id=', 4)
get_fid = lambda s: s[s.find(PARAM[0])+PARAM[1]:]
fids:Set[str] = set()
for url in urls:
    fid:str = get_fid(url)
    fids.add(fid+'\n')

# -- Write to file

with open('fids', 'w') as fp:
    fp.writelines(fids)
