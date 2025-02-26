# quickly makes an obsidian markdown for useful unicode characters
# https://unicode-explorer.com/list/arrows

import re

with open('input.txt', 'r') as file:
    data = file.read()

data = data.split('\n')
res = ''

for line in data:
    regex = re.match(r'https://unicode-explorer.com/c/([0-9a0fA-F]+)', line)
    if regex:
        hexstr = regex.group(1)
        unicode = chr(int(hexstr, 16))
        res += f'- `{unicode}` {unicode}  [0x{hexstr}]({line})'
    else:
        res += line
    res += '\n'

with open('output.md', 'w') as file:
    file.write(res)