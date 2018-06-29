import re
from Bio import Entrez
from Bio import Medline
from vector_space_modal import do_search
from ext_content import ext_relations


def get_data():
    terms = []
    with open('data/demo.bin', 'r') as inputFile:
        # loop through each line in file
        for line in inputFile:
            line = line.strip()
            terms.append(line)
    return terms


def ext_articles():
    result = get_data()
    max_count = 100
    relations = []
    for term in result:
        print(term)
        Entrez.email = 'A.N.Other@example.com'
        h = Entrez.esearch(db='pubmed', retmax=max_count, term=term, sort='pub date')
        result = Entrez.read(h)

        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='medline', retmode='text')
        records = Medline.parse(h)
        # print(records)

        abstracts = []
        for record in records:
            # print(record)
            pmid = record.get('PMC')
            ab = record.get('AB')
            if pmid:
                # print(pmid)
                abstracts.append((pmid, ab))
        # print(abstracts[0])
        article_ids = do_search(abstracts, term)
        for article_id in article_ids:
            extracted_relations = ext_relations(article_id, term)
            print(extracted_relations)
            print(len(extracted_relations))
            relations.append(extracted_relations)

    return relations


# ext_articles()
