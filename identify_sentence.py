import nltk
import re
from nltk.corpus import stopwords
from idintify_entities import identify_entities
from classifier import classify
from symptom_tagger.TextAnalyse.fuzzy import symptoms_tagger


ds_patterns = []
# open the relations files
with open('data/DS_relation_patterns.bin', 'r') as inputFile:
        # loop through each line in file
        for line in inputFile:
            line = line.strip()
            ds_patterns.append(line)


dg_patterns = []
# open the relations files
with open('data/DG_relation_patterns.bin', 'r') as inputFile2:
        # loop through each line in file
        for line in inputFile2:
            line = line.strip()
            dg_patterns.append(line)

stop_words = set(stopwords.words("english"))
Abstracts = ["" for x in range(6)]


def identify_sentences(disease, text):

    tagged_text = symptoms_tagger(text)
    context = nltk.sent_tokenize(tagged_text)
    content = ""
    for sent in context:
        regex1 = re.compile(r'<symptom>')
        regex2 = re.compile(r'<gene>')
        if regex1.search(sent):
            # print(sent)
            content += " " + sent

        elif regex2.search(sent):
            # print(sent)
            content += " " + sent

    # for disease, abstract in Abstracts:
    sentences = nltk.sent_tokenize(content)
    # extract_sentence = []
    ext_sent = ""
    ext_sent2 = ""
    for sent in sentences:
        line = re.sub(r'<\/?[^>]*>', '', sent)
        # print(line)
        category = classify(line)
        # print(category)
        if category:
            if category == "symptoms":
                ext_sent += " " + sent
            elif category == "gene":
                # print(sent)
                ext_sent2 += " " + sent
        else:
            # get d_s relation patterns and check with each sentences
            for pattern in ds_patterns:
                regex2 = re.compile(r'(?i)\b(%s)\b' % pattern)
                if regex2.search(line):
                    # print(sent)
                # if relation in sent:
                    ext_sent += " "+sent
                    break

            # get d_g relation patterns and check with each sentences
            for pattern in dg_patterns:
                regex3 = re.compile(r'(?i)\b(%s)\b' % pattern)
                if regex3.search(line):
                # if relation in sent:
                    ext_sent2 += " " + sent
                    break
    entity_set = identify_entities(disease, ext_sent, ext_sent2)
    return entity_set
#
# text = "It can make it hard to breathe, too, and can cause wheezing, fever, tiredness, and chest pain. The disease happens when the lining of the airways in your lungs gets irritated."
#
# identify_sentences("dengu", text)