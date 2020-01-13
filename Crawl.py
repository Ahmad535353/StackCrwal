from stackapi import StackAPI
import datetime, time
today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)
today_sec = time.mktime(today.timetuple())
week_ago_sec = time.mktime(week_ago.timetuple())
SITE = StackAPI('stackoverflow')
# tags = SITE.fetch('tags')
questions = SITE.fetch('questions', fromdate=int(week_ago_sec), todate=int(today_sec),
    tagged='Android', sort='creation')
f = open("1.txt", "w", encoding='utf8')
for question in questions['items']:
    f.write(str(question))
    f.write(str('\n'))
f.close()
print('done')
