import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import lxml
from celery import shared_task
from scraping.models import News
from urllib.parse import urlencode

from celery.schedules import crontab

from FinancialNews.celery import app

#scraping function
@app.task
def financialnews_rss():
    article_list = []
    try:
        print('Starting the scraping tool')
        symbols = ['AAPL', 'TWTR', 'GC=F(GOLD)', 'INTC']

        for s in symbols:
            headers = {'user-agent': 'Mozilla/5.0'}

            url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?'
            mydict = {'s': s, 'region' : 'US', 'lang' : 'en-US'}
            param = urlencode(mydict)

            r = requests.get(url + param, headers = headers)
            soup = BeautifulSoup(r.content, 'lxml')

            articles = soup.findAll('item')
            #print(articles)

            for a in articles:
                description = a.find('description').text
                guid = a.find('guid').text
                link = a.find('link').text
                pubDate_wrong = a.find('pubdate').text
                pubDate = datetime.strptime(pubDate_wrong, '%a, %d %b %Y %H:%M:%S %z')
                title = a.find('title').text

                # print (pubDate, pubDate_wrong)

                article = {
                    'description': description,
                    'guid': guid,
                    'link': link,
                    'pubDate': pubDate,
                    'title': title
                }

                article_list.append(article)

        print('Finished scraping the articles')

        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)


@app.task(serializer='json')
def save_function(article_list):
    print('starting')
    new_count = 0
    
    for article in article_list:
        try:
            News.objects.create(
                description = article['description'],
                guid = article['guid'],
                link = article['link'],
                pubDate = article['pubDate'],
                title = article['title']
            )
            new_count += 1
        except Exception as e:
            print('failed at latest_article is none')
            print(e)
            break
    return print('finished')


@app.task
def print_random():
    print("test")