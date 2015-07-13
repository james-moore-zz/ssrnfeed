"""Aggregates Duke Law SSRN feeds

Read SSRN CSV file
Open each SSRN feed
Read each SSRN feed
Return a time-sorted single feed
"""

import csv
import requests
import io
import feedparser
import time
import pprint
import datetime

def date_cutoff(time_cutoff=10)

    today = datetime.datetime.today()
    cutoff = today - datetime.timedelta(days= time_cutoff)

    return cutoff

def get_ssrn_csv():
    """Fetches CSV file from Google; returns a CSV reader"""
    x = requests.get('https://docs.google.com/spreadsheets/d/1XF9S33GnFBqh2B4lABzYkBxNAtXmia-qAiGtCxX1a8s/export?gid=0&format=csv')
    f = io.StringIO(x.text)
    reader = csv.DictReader(f)
    # print(reader.fieldnames)
    return reader

def main():
    """For each CSV row: do something"""
    date_cutoff()     #where we establish a cut off for the date
    reader = get_ssrn_csv()
    for row in reader:
        # print(row['rss'])
        d = feedparser.parse(row['rss'])
        pprint.pprint(d['feed'])
        pprint.pprint(d['feed']['author'])

    RSS = []

    for item in reader:
        if item.date > cutoff:
            RSS.append(item)
    RSS.sort(reverse=true)      #This should short the RSS feed list by most recent.

    time.sleep(2.0)
    
    # TODO: output into XML
    return RSS

if __name__ == '__main__':
    main()
