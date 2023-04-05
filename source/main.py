from hashlib import md5

from app import application
from get_data import get_data
from block_device import block
from foundNewDevice import found_new_device

while True:
    if found_new_device():

        # application(device_id=md5(a[-1].encode()).hexdigest(),
        #             device_type=a[0]['Type'],
        #             device_name=a[0]['Name'],
        #             devices=blocked_devices
        #             )
