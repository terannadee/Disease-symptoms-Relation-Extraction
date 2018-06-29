import pickle
import nltk
from nltk.tokenize import word_tokenize


def word_feats_extrnl(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


def find_features(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


def classify(centence):
    # print(centence)
    classifier_f = open("naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f)
    feats = find_features(centence)
    for sample in classifier.prob_classify(feats).samples():
        if classifier.prob_classify(feats).prob(sample) > 0.65:
            # print(sample, classifier.prob_classify(feats).prob(sample))
            return sample

    classifier_f.close()

# words = "Symptoms include coughing up mucus, wheezing, shortness of breath, and chest discomfort."
# print(classify(words))