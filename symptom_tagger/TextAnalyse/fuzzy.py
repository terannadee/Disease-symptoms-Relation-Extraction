import re

from symptom_tagger.TextAnalyse.text_preprocessing import main_text
genes_list = []
symptoms_list = []

with open('symptom_tagger/TextAnalyse/genes.txt', 'r') as inputFile1:
    # loop through each line in file
    for line in inputFile1:
        line = line.strip()
        # print(line)
        genes_list.append(line)


with open('symptom_tagger/TextAnalyse/symptoms_v3.txt', 'r') as inputFile:
    # loop through each line in file
    for line in inputFile:
        line = line.strip()
        symptoms_list.append(line)


def match_symptoms(search):

    """Get the perfect symptom matches related to the search phrases"""

    text = ""

    for item in search:
        sentence = re.sub(r'<\/?[^>]*>', '', item)
        # print("1st")
        # print(sentence)
        pattern = r'<c>(.*?)<\/c>'
        noun_prases = re.findall(pattern, item, flags=0)
        # print(symptoms)
        for s in noun_prases:
            # new_sent = ""
            for symptom in symptoms_list:
                if symptom.lower() == s.lower():
                    # print token
                    sentence = sentence.replace(s, "<symptom>" + s + "</symptom>", 1)
                    break
        text += ' '+sentence
    # print(text)
    return text


def symptoms_tagger(x):

    search = main_text(x)

    tagged_symptom_list = match_symptoms(search)
    return tagged_symptom_list
