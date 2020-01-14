from flask import Flask, request, render_template
from Crawl import fetch_results
app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def divide():
    number = None
    questions_by_time = None
    questions_by_votes = None
    if request.method == 'POST':
        number = request.form['number']
        if number is '':
            number = 10
        else:
            number = int(number)
        days = request.form['days']
        if days is '':
            days = 7
        else:
            days = int(days)
        questions_by_time, questions_by_votes = fetch_results(number, days)
        # divide_by = float(request.form['divide_by'])

    return render_template('index.html', num_of_results=number, questions_by_time=questions_by_time,
                           questions_by_vote=questions_by_votes)


if __name__ == '__main__':
    app.debug = True
    app.run()
