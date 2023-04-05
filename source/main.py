from hashlib import md5
from os import path

from app import application
from block_device import block
from foundNewDevice import found_new_device
from get_data import get_data


while True:
    if ids := list(found_new_device('/'.join(path.abspath('main.py').split('/')[:-2]))):
        block(ids)
        a = list(get_data())
        for data in a:
            application(device_id=md5(data[-1].encode()).hexdigest(),
                        path='/'.join(path.abspath('main.py').split('/')[:-1]),
                        device_type=data[0]['Type'],
                        device_name=data[0]['Name'],
                        devices=ids,
                        )
