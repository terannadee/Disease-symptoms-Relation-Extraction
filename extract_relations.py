from googleapiclient.discovery import build
import urllib3
from bs4 import BeautifulSoup
import nltk
from identify_sentence import identify_sentences
import re

# http://cse.google.com/
my_api_key = "AIzaSyBvXH583ijsh2TG4gs1LqcC4g86uk_G0ck"
my_cse_id = "002650997601401057776:hrwppggkwls"


# open the files
def get_data():
    terms = []
    with open('data/demo.bin', 'r') as inputFile:
        # loop through each line in file
        for line in inputFile:
            line = line.strip()
            terms.append(line)

    a = set(terms)
    seen = set()
    result = []
    for item in a:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return terms


# google search
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


def do_search():
    terms = get_data()
    relations = []
    for search_term in terms:
        print(search_term)
        results = google_search(search_term, my_api_key, my_cse_id, num=10)
        for result in results:
            # print result
            link = result.get('link')
            # print(link)

            urllib3.disable_warnings()
            hdr = {
                'User-Agent': 'Mozilla/5.0 ',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

            http = urllib3.PoolManager()
            req = http.request('GET', link, headers=hdr)

            try:
                req.data
            except urllib3.exceptions as e:
                if e.code == 401:
                    print('not authorized')
                elif e.code == 404:
                    print('not found')
                elif e.code == 503:
                    print('service unavailable')
                else:
                    print('unknown error: ')
            else:
                response = req.data
                soup = BeautifulSoup(response, "lxml")

                # print(soup)
                for tags in soup.find_all('li'):
                    tags.append(", ")
                for tags in soup.find_all('ul'):
                    tags.append(".")

                # remove all script and style elements
                for script in soup(["script", "style", "noscript", "sup", "h1", "h2", "nav", "table", "aside", "footer", "header"]):
                    script.extract()
                for div in soup.find_all("div", {'class': 'vs_wrapper'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'headlines_split'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'sidebar'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'from_webmd'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'sideBox'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'footer_rdr'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'mwe-popups-container'}):
                    div.decompose()
                for div in soup.find_all("div", {'class': 'toc'}):
                    div.decompose()
                # select <p> tags and get content
                content = ""
                texts = soup.find_all(['p', 'ul'])

                # print(texts)
                for text in texts:
                    content += " " + text.get_text()

                # remove space
                lines = (line.strip() for line in content.splitlines())
                # create paragraph
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines and join
                text = ' '.join(chunk for chunk in chunks if chunk)
                print(text)

                extracted_relations = identify_sentences(search_term, text)
                # show_relations(extracted_relations)
                print(extracted_relations)
                print(len(extracted_relations))
                # print(re.sub(r'[\[A-Z0-9\'\]]','', str(extracted_relations)))
                relation = []
                for r in extracted_relations:
                    relation.append(re.sub(r'[\[A-Z0-9\,\'\]]','',str(r)))
                relations.append(re.sub(r'[A-Z0-9\']','',str(relation)))

    return relations



# do_search()
