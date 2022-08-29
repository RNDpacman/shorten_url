import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def get_short(long_url: str, token) -> str:
    '''
    Возвращает сокращенную версию long_url
    '''
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': token}
    payload = {'long_url': long_url}
    shorten_url = requests.post(api_url, json=payload, headers=headers)
    shorten_url.raise_for_status()

    return shorten_url.json()['link']


def get_clicks(bitlink: str, token) -> int:
    '''
    Возвращает суммарное количество кликов для bitlink
    '''

    parsed_url = urlparse(bitlink)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary'
    headers = {'Authorization': token}
    clicks = requests.get(api_url, headers=headers)
    clicks.raise_for_status()

    return clicks.json()['total_clicks']


def is_bitlink(url: str, token) -> bool:
    '''
    Является ли url корректным bitlink
    '''

    headers = {'Authorization': token}
    parsed_url = urlparse(url)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}'
    bitlink_info = requests.get(api_url, headers=headers)

    return bitlink_info.ok


def main():

    env_name = 'BITLY_TOKEN'

    if load_dotenv() and os.getenv(env_name):
        token = os.getenv(env_name)
    else:
        raise Exception('You did not specify a token')


    url = input('Enter your url: ')

    if is_bitlink(url, token=token):
        try:
            clicks = get_clicks(url, token=token)
        except requests.exceptions.HTTPError:
            print('Error: check url')
        else:
            print('Total clicks:', clicks)
    else:
        try:
            short_url = get_short(long_url=url, token=token)
        except requests.exceptions.HTTPError:
            print('Error: Check your url')
        else:
            print('Your shorten url:', short_url)


if __name__ == '__main__':
    main()
