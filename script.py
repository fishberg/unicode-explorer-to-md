# quickly makes an obsidian markdown for useful unicode characters
# https://unicode-explorer.com/list/arrows

import re

with open('data.txt', 'r') as file:
    data = file.read()

data = data.split('\n')
res = ''

for line in data:
    regex = re.match(r'https://unicode-explorer.com/c/([0-9a0fA-F]+)', line)
    if regex:
        res += chr(int(regex.group(1), 16))
        res += f' [X]({line})'
    else:
        res += line
    res += '\n'

print(res)