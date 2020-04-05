from flask import Flask, render_template
import lotto


app = Flask(__name__)


@app.route('/connect')
def test():
    # connection test
    return 'success'



# index 페이지 출력
@app.route('/')
def index():
    return render_template('./index.html')


@ app.route('/get_win_numbers/<int:round_number>')
def get_win_number(round_number):
    round_date, win_number_list, bonus_number, win_amt = lotto.get_win_numbers(round_number)
    return render_template('./get_win_numbers.html',
                           round_number=round_number)








if __name__ == '__main__':
    app.run(debug=True)