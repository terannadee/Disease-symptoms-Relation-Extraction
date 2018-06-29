import re


def tuple_generate(disease, s_result, g_result):
    tuple_set = []
    for symptom in s_result:
        tuple_set.append([str(re.sub('[^a-zA-Z]+', '_', disease.lower()).rstrip("_")), 'has_symptom',
                          str(re.sub('[^a-zA-Z]+', '_', symptom.lower()).rstrip("_"))])

    for gene in g_result:
        tuple_set.append([str(re.sub('[^a-zA-Z]+', '_', disease.lower()).rstrip("_")), 'associate_with_gene',
                          str(re.sub('[^a-zA-Z]+', '_', gene.lower()).rstrip("_"))])
    return tuple_set
