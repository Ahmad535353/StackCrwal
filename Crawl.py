from stackapi import StackAPI
import datetime
import time
import pickle


def fetch_results(number_of_results, days):

    if number_of_results > 20:
        number_of_results = 20
    if days < 0 or number_of_results < 0:
        return None, None
    if number_of_results == 0 or days == 0:
        number_of_results = 10
        days = 7

    # with open('questions_time.pickle', 'rb') as data:
    #     questions = pickle.load(data)
    # with open('questions_vote.pickle', 'rb') as data:
    #     questions_by_vote = pickle.load(data)
    # return questions, questions_by_vote


    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=days)
    today_sec = time.mktime(today.timetuple()) + 86400
    week_ago_sec = time.mktime(week_ago.timetuple())
    SITE = StackAPI('stackoverflow')
    SITE.page_size = number_of_results
    SITE.max_pages = 1
    # tags = SITE.fetch('tags')
    questions = SITE.fetch('questions', fromdate=int(week_ago_sec), todate=int(today_sec),
                           tagged='Android', sort='creation', filter='!9YdnSIN*P')
    questions = questions['items']
    questions_by_vote = SITE.fetch('questions', fromdate=int(week_ago_sec), todate=int(today_sec),
                           tagged='Android', sort='votes', filter='!9YdnSIN*P')
    questions_by_vote = questions_by_vote['items']

    print('Done fetching.')
    # with open('questions_time.pickle', 'wb') as output:
    #     pickle.dump(questions, output)
    # with open('questions_vote.pickle', 'wb') as output:
    #     pickle.dump(questions_by_vote, output)

    return questions, questions_by_vote

number = 2
days = 7
fetch_results(number, days)