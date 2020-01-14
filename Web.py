from flask import Flask, render_template
from Crawl import fetch_results
app = Flask(__name__)


# def foo():
#     # Do something
#     return bar  # In this example, foo can return a string, list or dict


@app.route('/')
def index():
    questions_by_time, questions_by_votes = fetch_results()
    return render_template('index.html', questions_by_time=questions_by_time, questions_by_vote=questions_by_votes)


if __name__ == '__main__':
    app.run(debug=True)