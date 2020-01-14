from stackapi import StackAPI
import datetime
import time
import pickle


def fetch_results():
    # test_dict = dict()
    # test_dict['title'] = 'ahmad'
    # test_dict['body'] = 'ahmad ahmadahmadahma dahmadahmadahma dahmadahmadahma dahmadahmadahmad ' \
    #                     'ahmadahmadahmadahma dahmadahmadahmadahmada hmadahmadahmadahmadahmad' \
    #                     'ahmadahmada hmadahmada hmadahmadahmadahma dahmadahmadahmadahmadahmad'
    # questions = [test_dict]
    # return questions
    #
    # with open('questions_time.pickle', 'rb') as data:
    #     questions = pickle.load(data)
    # with open('questions_vote.pickle', 'rb') as data:
    #     questions_by_vote = pickle.load(data)
    # return questions, questions_by_vote


    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)
    today_sec = time.mktime(today.timetuple()) + 86400
    week_ago_sec = time.mktime(week_ago.timetuple())
    SITE = StackAPI('stackoverflow')
    SITE.page_size = 10
    SITE.max_pages = 1
    # tags = SITE.fetch('tags')
    questions = SITE.fetch('questions', fromdate=int(week_ago_sec), todate=int(today_sec),
                           tagged='Android', sort='creation', filter='!9YdnSIN*P')
    questions = questions['items'][:10]
    questions_by_vote = SITE.fetch('questions', fromdate=int(week_ago_sec), todate=int(today_sec),
                           tagged='Android', sort='votes', filter='!9YdnSIN*P')
    questions_by_vote = questions_by_vote['items'][:10]

    print('Done fetching.')
    # with open('questions_time.pickle', 'wb') as output:
    #     pickle.dump(questions, output)
    # with open('questions_vote.pickle', 'wb') as output:
    #     pickle.dump(questions_by_vote, output)

    return questions, questions_by_vote

fetch_results()