import os
import re
from hashlib import md5


def get_data(pwd) -> tuple[dict, str]:
    data = {}
    os.system(f'lsusb > {pwd}/files/data.txt')
    with open(f'{pwd}/files/data.txt') as file, open(f'{pwd}/files/ids.txt') as ids:
        for i in file.read().strip().split('\n'):
            if 'hub' in i.lower():
                continue
            i = re.split(' ', i, 6)
            data[i[5]] = {'Bus': i[1],
                          'Device': i[3][:-1],
                          'Type': 'Drive' if 'drive' in i[-1].lower() else 'Keyboard' if 'keyboard' in i[-1].lower()
                          else 'Mouse' if 'mouse' in i[-1].lower() else 'Input Device',
                          'Name': i[-1]
                          }
        ids = set(ids.read().split('\n'))
        for k in data.keys():
            if md5(k.encode()).hexdigest() not in ids:
                yield data[k], k


if __name__ == '__main__':
    pwd = input()
    with open(f'{pwd}/files/ids.txt', 'a') as ids:
        for i in get_data(pwd):
            ids.write(f"{md5(i[1].encode()).hexdigest()}\n")
