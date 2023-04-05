import os


def block(info: iter):
    for i in info:
        os.system(f'xinput disable {i}')
