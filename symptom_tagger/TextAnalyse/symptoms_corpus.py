

def loading_values():
    symptoms_list = []
    f = open('symptom_tagger/TextAnalyse/symptoms_v3.txt', 'r')
    # symptoms_list = []
    for line in f:
        # phrases = list(map(lambda x: x.strip(), line.split(',')))
        symptoms_list.append(line)

    return symptoms_list

