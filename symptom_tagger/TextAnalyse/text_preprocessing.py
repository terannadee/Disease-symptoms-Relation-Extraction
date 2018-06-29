import nltk
import re
# from geniatagger import GeniaTagger
from nltk.corpus import stopwords
from textblob import TextBlob


def prepareForNLP(text):

    """Tokenize the sentences and output the word tokens.
            use the nltk pos tagger to tag the word tokenze. """
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sent) for sent in sentences]
    tagged_words = [nltk.pos_tag(sent) for sent in word_tokens]
    return tagged_words


def chunk(text):
    """ Return the noun phrases using reguler expressoins"""

    '''pattern = ['JJ', 'NN', 'VB', 'NN']
        matches = []

        for i in range(len(tagged)):
            if tagged[i:i+len(pattern)] == pattern:
                matches.append(sentences[i:i+len(pattern)])

        matches = [' '.join(match) for match in matches]
        print(matches)'''

    grammar = """NP: {<V.*>+(<RP?><NN>)?}
                NP: {(<NN.*><DT>)?(<NN.*><IN>)?<NN.*>?<JJ.>*<NN.*>+}
                NP: {<V.*>}
                ENTITY: {<NN.*>}"""

    parser = nltk.RegexpParser(grammar)
    result = parser.parse(text)
    t_sent = ' '.join(word for word, pos in text)
    for subtree in result.subtrees():
        # print(subtree)
        if subtree.label() == 'NP':
            noun_phrases_list = ' '.join(word for word, pos in subtree.leaves())
            t_sent = t_sent.replace(noun_phrases_list, "<c>"+noun_phrases_list+"</c>", 1)
    # print(t_sent)
    return t_sent


def main_text(full_text):
    sentence = full_text.replace('"','')
    sentences = prepareForNLP(sentence)
    chunk_sent = []
    for sentence in sentences:
        chunk_sent.append(chunk(sentence))
    return chunk_sent

