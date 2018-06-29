import nltk
from textblob import TextBlob
import re
from tuple_generation import tuple_generate


def identify_entities(disease, sentence, sentence2):
    pattern1 = r"<symptom>(.*?)</symptom>"
    symptoms = re.findall(pattern1, sentence, flags=0)

    pattern2 = r"<gene>(.*?)</gene>"
    genes = re.findall(pattern2, sentence2, flags=0)

    a = set(symptoms)
    b = set(genes)

    s_result = remove_duplicates(a)
    g_result = remove_duplicates(b)

    tuples = tuple_generate(disease, s_result, g_result)
    return tuples


def remove_duplicates(a):
    new_list = []
    for item in a:
        if item.lower() not in new_list:
            new_list.append(item.lower())
    return new_list
