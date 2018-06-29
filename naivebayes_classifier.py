import pickle
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from sklearn.naive_bayes import MultinomialNB


def word_feats_extrnl(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


def find_features(words):
    return dict([(word, True) for word in nltk.trigrams(word_tokenize(words))])


symptoms = []
gene = []


with open("symptom_relations_text.txt", encoding='utf-8', errors='ignore')as f:
    for line in f:
        line = line.strip()
        symptoms.append((word_feats_extrnl(line.lower()), 'symptoms'))

with open("gene_relation_text.txt", encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        gene.append((word_feats_extrnl(line.lower()), 'gene'))


# print(symptoms)
# print(gene)
len_of_symptoms = int(len(symptoms) * 4 / 5)
len_of_genes = int(len(gene) * 4 / 5)

training_set = symptoms[:len_of_symptoms] + gene[:len_of_genes]
testing_set = symptoms[len_of_symptoms:] + gene[len_of_genes:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

print("naive bayes accuracy",(nltk.classify.accuracy(classifier,testing_set))*100)


save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

#
# def classifier(centence):
#     classifier_f = open("naivebayes.pickle", "rb")
#     classifier = pickle.load(classifier_f)
#     feats = find_features(centence)
#     for sample in classifier.prob_classify(feats).samples():
#         print(sample, classifier.prob_classify(feats).prob(sample))
#         if classifier.prob_classify(feats).prob(sample) > 0.75:
#             return sample
#
#     classifier_f.close()
#
# words = "The combination of severe vomiting and diarrhea often leads to severe dehydration."
# print(classifier(words))

#
# MNB_classifier = nltk.SklearnClassifier(MultinomialNB())
# MNB_classifier.train(training_set)
# print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)
#
# save_classifier = open("mnb.pickle","wb")
# pickle.dump(MNB_classifier, save_classifier)
# save_classifier.close()
# #
# # print("naive bayes accuracy",(nltk.classify.accuracy(classifier,testing_set))*100)
# # print(classifier.show_most_informative_features(15))
# #
# classifier_f = open("mnb.pickle", "rb")
# classifier = pickle.load(classifier_f)
#
# words = "Once you have the trained model, you can use the function predict to classify your test data into one of the classes."
# feats = find_features(words)
# print(classifier.prob_classify(feats))