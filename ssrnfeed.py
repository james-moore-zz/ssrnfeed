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

def get_ssrn_csv():
    """Fetches CSV file from Google; returns a CSV reader"""
    x = requests.get('https://docs.google.com/spreadsheets/d/1XF9S33GnFBqh2B4lABzYkBxNAtXmia-qAiGtCxX1a8s/export?gid=0&format=csv')
    f = io.StringIO(x.text)
    reader = csv.DictReader(f)
    # print(reader.fieldnames)
    return reader

def main():
    """For each CSV row: do something"""
    reader = get_ssrn_csv()
    for row in reader:
        # print(row['rss'])
        d = feedparser.parse(row['rss'])
        pprint.pprint(d['feed'])
        pprint.pprint(d['feed']['author'])
        #for entry in d.entries:
        #    print(entry.title)
        time.sleep(2.0)
    return None

if __name__ == '__main__':
    main()
