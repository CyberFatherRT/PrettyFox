import os


def block(info: dict):
    ids = []
    if info['Type'] != 'Drive':
        os.system('xinput > files/newDevices.txt')
        with open('files/newDevices.txt') as devices:
            devices = [i.strip(' ↳⎣⎜⎡\n') for i in devices.readlines()]
            for i in info['Name'].split():
                for j in devices:
                    if i in j:
                        j = j.split('\t')[1][3:]
                        os.system(f'xinput disable {j}')
                        ids.append(j)
    return tuple(ids)
