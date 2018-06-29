from evaluations.classifier2 import classify


def get_correct_data():
    test_data = []

    with open("testing_true_data.txt", encoding='utf-8', errors='ignore')as f:
        for line in f:
            line = line.strip()
            test_data.append(line)

    return test_data


def get_wrong_data():
    test_data = []

    with open("testing_false data.txt", encoding='utf-8', errors='ignore')as f:
        for line in f:
            line = line.strip()
            test_data.append(line)

    return test_data


def evaluations1():
    sentences = get_correct_data()
    # print(sentences)
    print(classify(sentences))


def evaluations2():
    sentences = get_wrong_data()
    print(classify(sentences))


evaluations2()