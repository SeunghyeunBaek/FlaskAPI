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

    return round_number, round_date, win_number, bonus_number, win_amt


def generate_random_numbers():
    random_number_list = sorted(random.sample(range(1, 47), 6))
    return random_number_list


def get_rank(win_numbers, bonus_number, random_numbers):
    win_count = len(set(win_numbers).intersection(random_numbers))
    bonus_count = 1 if bonus_number in random_numbers else 0
    if win_count == 6:
        rank = 1
    elif win_count == 5 and bonus_count == 1:
        rank = 2
    elif win_count == 5:
        rank = 3
    elif win_count == 4:
        rank = 4
    elif win_count == 3:
        rank = 5
    else:
        rank = -1

    return rank, win_count, bonus_count


def simulate_lotto(round_number, max_buy_count):
    round_number, round_date, win_number_list, bonus_number, win_amt = get_win_numbers(round_number)
    buy_count = 0
    buy_amt = 0
    win_count_list = [0 for i in range(5)]

    while buy_count < max_buy_count:

        random_number_list = generate_random_numbers()
        buy_count += 1
        buy_amt = buy_count * 1000
        rank, win_count, bonus_count = get_rank(win_number_list, bonus_number, random_number_list)

        if rank == 1:
            win_count_list[rank-1] += 1
            break

        elif rank != -1:
            win_count_list[rank-1] += 1
        else:
            pass

    for rank in range(5):
        print(f'{rank+1} rank: {win_count_list[rank]}')
    return None


if __name__ == '__main__':
    simulate_lotto(3)
