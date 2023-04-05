import os


def found_new_device(path):
    os.system(f'xinput > {path}/files/newDevices.txt')
    with open(f'{path}/files/newDevices.txt') as new_devices, open(f'{path}/files/oldDevices.txt') as old_devices:
        if new_devices.read() == old_devices.read():
            return False
        new_devices.seek(0)
        old_devices.seek(0)
        new_devices = [i.strip(' ⎜⎡⎣↳\n').split('\t') for i in new_devices.readlines()]
        old_devices = [i.strip(' ⎜⎡⎣↳\n').split('\t')[0].strip() for i in old_devices.readlines()]
        for i in new_devices:
            if i[0].strip() not in old_devices:
                yield i[1][3:]
