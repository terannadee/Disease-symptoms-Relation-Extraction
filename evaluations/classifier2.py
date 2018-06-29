import pickle
import nltk
from nltk.tokenize import word_tokenize


def word_feats_extrnl(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


def find_features(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


def classify(sentences):
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    i = 0
    for sentence in sentences:
        # print(sentence)

        feats = find_features(sentence)
        for sample in classifier.prob_classify(feats).samples():
            if classifier.prob_classify(feats).prob(sample) > 0.8:
                # print(sample, classifier.prob_classify(feats).prob(sample))
                # print(sentence)
                i = i+1
    return i

    # classifier_f.close()

# words = "Symptoms include coughing up mucus, wheezing, shortness of breath, and chest discomfort. "
# print(classify(words))