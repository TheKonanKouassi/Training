from bs4 import BeautifulSoup

import requests

import csv

# try:
#
#     with open('../data/simple.html') as html_file:
#
#         soup = BeautifulSoup(html_file, 'lxml')
#
# except FileNotFoundError as e:
#
#     print(str(e))
#
# for article in soup.find_all('div', class_ = 'article'):
#
#     headline  = article.h2.a.text
#
#     print(headline)
#
#     summary = article.p.text
#
#     print(summary)
#
#     print()


# ============================================================================#
# Scrape from _threading_local website

pages = range(1, 13)

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline', 'summary', 'video_link'])

for page in pages:

    url = f'http://coreyms.com/page/{page}'

    try:

        source = requests.get(url).text

        soup = BeautifulSoup(source, 'lxml')

    except Exception as e:

        print(str(e))

    for article in soup.find_all('article'):

        try:

            headline = article.h2.a.text

        except Exception:

            headline = None

        try:

            summary = article.find('div', class_ = 'entry-content')

        except Exception:

            summary = None

        try:

            vid_scr = article.find('iframe', class_ = 'youtube-player')['src']

            vid_id = str.split(str.split(vid_scr, '/')[4], '?')[0]

            yt_link = f'https://www.youtube.com/watch?v={vid_id}'

        except Exception:

            yt_link = None

        csv_writer.writerow([headline, summary.text, yt_link])

        # TODO: Need to add try excep bloc

csv_file.close()

#my_dict = dict(('healines' : healines, summaries, ))
