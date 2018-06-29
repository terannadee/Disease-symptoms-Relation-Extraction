import re

from fuzzywuzzy import process as fzproc, fuzz, process
import random
from symptom_tagger.TextAnalyse.disease_corpus import remove_duplicates, disease_list
from symptom_tagger.TextAnalyse.symptoms_corpus import loading_values
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


def fuzzy_match_genes(item, tagged):

    pattern = r'<c>(.*?)<\/c>'
    noun_prases = re.findall(pattern, item, flags=0)
    # print(symptoms)
    for s in noun_prases:
        for gene in genes_list:
            if gene.lower() == s.lower():
                # print(s)
                # print(gene)
                tagged = tagged.replace(s, "<gene>" + s + "</gene>", 1)
                break
    return tagged


def fuzzy_match_symptoms(dictionary1, search):

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

        sentence = fuzzy_match_genes(item,sentence)
        text += ' '+sentence
    # print(text)
    return text


def iterative_levenshtein(s, best, **weight_dict):
    """
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t

        weight_dict: keyword parameters setting the costs for characters,
                     the default value for a character will be 1
    """

    rows = len(s) + 1
    cols = len(best) + 1

    alphabet = "abcdefghijklmnopqrstuvwxyzABCD"
    w = dict((x, (1, 1, 1)) for x in alphabet + alphabet.upper())
    if weight_dict:
        w.update(weight_dict)

    dist = [[0 for x in range(cols)] for x in range(rows)]
    # source prefixes can be transformed into empty strings
    # by deletions:
    for row in range(1, rows):
        dist[row][0] = dist[row - 1][0] + w[s[row - 1]][0]
    # target prefixes can be created from an empty source string
    # by inserting the characters
    for col in range(1, cols):
        dist[0][col] = dist[0][col - 1] + w[best[col - 1]][1]

    for col in range(1, cols):
        for row in range(1, rows):
            deletes = w[s[row - 1]][0]
            inserts = w[best[col - 1]][1]
            subs = max((w[s[row - 1]][2], w[best[col - 1]][2]))
            if s[row - 1] == best[col - 1]:
                subs = 0
            else:
                subs = subs
            dist[row][col] = min(dist[row - 1][col] + deletes,
                                 dist[row][col - 1] + inserts,
                                 dist[row - 1][col - 1] + subs)  # substitution
    for r in range(rows):
        print(dist[r])

    return dist[row][col]


def benchmark_fuzzy_match(x):

    search = main_text(x)
    # print(search)

    dictionary = remove_duplicates(disease_list())
    rnd = random.Random(0)
    rnd.shuffle(dictionary)

    dictionary1 = loading_values()
    # print(dictionary1)
    rnd = random.Random(0)
    rnd.shuffle(dictionary1)

    # tagged_disease_list = fuzzy_match_diseases(dictionary, search)
    tagged_symptom_list = fuzzy_match_symptoms(dictionary1, search)
    return tagged_symptom_list


if __name__ == '__main__':
    benchmark_fuzzy_match()
    # tagging_symptoms()
