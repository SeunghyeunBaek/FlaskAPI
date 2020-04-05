import requests
import json
import random


def get_win_numbers(round_number):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round_number}'
    lotto_dict = json.loads(s=requests.get(url).text)

    if lotto_dict['returnValue'] == 'fail':
        msg = f'round {round_number} is not completed'
        return msg

    else:
        round_date = lotto_dict['drwNoDate']

        # win numbers
        win_number = sorted([win_numbers for key, win_numbers in lotto_dict.items() if 'drwtNo' in key])
        bonus_number = lotto_dict['bnusNo']
        win_amt = lotto_dict['firstWinamnt']

    return round_date, win_number, bonus_number, win_amt


if __name__ == '__main__':
    print(type(get_win_numbers(3)))
