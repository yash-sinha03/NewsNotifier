from win10toast import ToastNotifier
import feedparser
import time

toaster= ToastNotifier()

fp= feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

for news in fp['items']:
    toaster.show_toast(
        title=news['title'],
        msg=news['summary'],
        duration=5
    )
    time.sleep(10)