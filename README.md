# StackCrwal
StackCrwal is a crawler which utilizes the StackAPI to search and display the latest and most-voted Android related questions in as many recent days as the client demands. The number of the results is also can be chosen by the client, but due to the traffic restrictions of different sites, I decided to put a 20 result limit per request.

After choosing the limits (if you don't choose, default values are 10 results for 7 recent days), the searching process will start and as soon as it fetched the data, the results will be available on the same page.

The results will be the title of the questions and by clicking on any one of them, you will be redirected to the main page.

I wanted to stay loyal to the task and don't go so much further, but due to the modularity of the code, it is very easy to add other features like tag-choosing and different sorting order and topics (for example make it ascending or search in a specific period in the past or most-commented questions, etc.)

You can build the website locally by running the Web.py using Python 3.5 (tested on windows 10 and chrome browser).
You need to install Flask framework and the StackAPI as well.
