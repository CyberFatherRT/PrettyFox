from hashlib import md5

from app import application
from block_device import block
from foundNewDevice import found_new_device
from get_data import get_data

pwd = input()
while True:
    if ids := list(found_new_device(pwd)):
        block(ids)
        for data in list(get_data(pwd)):
            application(device_id=md5(data[-1].encode()).hexdigest(),
                        path=pwd,
                        device_type=data[0]['Type'],
                        device_name=data[0]['Name'],
                        devices=ids,
                        )
