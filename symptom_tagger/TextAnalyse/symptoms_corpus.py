'''def main(file):

    with open(file, 'r') as f:
        reader = csv.reader(f)
        symptom_list = list(reader)
        return symptom_list
        #print(symptom_list)
        #print(len(symptom_list))


main('Symptoms.csv')'''


def loading_values():
    symptoms_list = []
    f = open('symptom_tagger/TextAnalyse/symptoms_v3.txt', 'r')
    # symptoms_list = []
    for line in f:
        # phrases = list(map(lambda x: x.strip(), line.split(',')))
        symptoms_list.append(line)

    return symptoms_list
    # print(symptoms_list)
    # print(results[0])


loading_values()


# def symptoms_list():
#     result = loading_values()
#     return result
