import urllib3
import nltk
from bs4 import BeautifulSoup
from identify_sentence import identify_sentences


def ext_relations(pmc_id, term):
        site = 'https://www.ncbi.nlm.nih.gov/pmc/articles/%s/' % pmc_id
        print(site)
        urllib3.disable_warnings()
        hdr = {
            'User-Agent': 'Mozilla/5.0 ',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

        http = urllib3.PoolManager()
        req = http.request('GET', site, headers=hdr)
        # print(req)
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

            # remove all script and style elements
            for script in soup(["script", "style", "noscript", "a", "form", "span", "sup", "h1", "h2"]):
                script.extract()
            # select <p> tags and get content
            content = ""
            texts = soup.find_all('p')
            for text in texts:
                content += " " + text.get_text()

            # remove space
            lines = (line.strip() for line in content.splitlines())
            # create paragraph
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines and join
            text = ' '.join(chunk for chunk in chunks if chunk)
            print(text)
            extracted_relations = identify_sentences(term, text)
            return extracted_relations

