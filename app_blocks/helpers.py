import ast
import requests


def get_blocks(date=''):
    if date:
        request = requests.get(f'https://bcschain.info/api/blocks?date={date}').text
    else:
        request = requests.get(f'https://bcschain.info/api/blocks').text
    return ast.literal_eval(request)


def get_block(height):
    request = requests.get(f'https://bcschain.info/api/block/{height}')
    if request.status_code != 200:
        return False
    return ast.literal_eval(request.text)
