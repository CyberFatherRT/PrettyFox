import os


def found_new_device():
    os.system('xinput > ../files/newDevices.txt')
    with open('../files/newDevices.txt') as new_devices, open('../files/oldDevices.txt') as old_devices:
        if new_devices.read() == old_devices.read():
            return False
        return True
