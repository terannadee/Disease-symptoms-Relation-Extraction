import nltk
import re
# from geniatagger import GeniaTagger
from nltk.corpus import stopwords
from textblob import TextBlob


def removeDigits(text):

    """Remove digits from the text"""

    answer = []
    for char in text:
        if not char.isdigit():
            answer.append(char)
    return ''.join(char)


def remove_urls(text):

    """Remove the URLs from the text"""

    '''text = re.sub(r'(?:(?:http|https):\/\/)?([-a-zA-Z0-9.]{2,256}\.[a-z]{2,4})\b(?:\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?', "",
                  text, flags=re.MULTILINE)
    text = '\n'.join([a for a in text.split("\n") if a.strip()])
    return text'''

    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    return text

    '''rep = re.compile(r"""
                                http[s]?://.*?\s
                                |www.*?\s
                                |(\n)
                                """, re.X)
    non_asc = re.compile(r"[^\x00-\x7F]")
    for line in text:
        non = non_asc.search(line)
        if non:
            continue
        m = rep.search(line)
        if m:
            line = line.replace(m.group(), "")
            if line.strip():
                print(line.strip())'''


def remove_smiles(text):

    """ Remove the Smiles from the text"""

    '''emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", text)
    return emoji_pattern'''
    emoji_pattern = re.compile(
        "["u"\U0001F600-\U0001F64F" u"\U0001F300-\U0001F5FF" u"\U0001F680-\U0001F6FF"  u"\U0001F1E0-\U0001F1FF""]+",
        flags=re.UNICODE)
    return emoji_pattern


def remove_stopwords(word_tokens):

    word_token = nltk.word_tokenize(word_tokens)
    stop_words = set(stopwords.words('english'))
    filtered_sentence = ''

    for w in word_token:
        if w not in stop_words:
            filtered_sentence += w + ' '
    return filtered_sentence



def prepareForNLP(text):

    """Tokenize the sentences and output the word tokens.
            use the nltk pos tagger to tag the word tokenze. """
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sent) for sent in sentences]
    tagged_words = [nltk.pos_tag(sent) for sent in word_tokens]
    # tagger = GeniaTagger('./geniatagger/geniatagger')
    # tagged_words = tagger.parse(word_tokens)
    return tagged_words
    # print(tagged_words)


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


def remove_duplicates(text):

    output = []
    seen = set()
    for value in text:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
    # print(output)


def main_text(full_text):
    sentence = full_text.replace('"','')
    sentences = prepareForNLP(sentence)
    chunk_sent = []
    for sentence in sentences:
        chunk_sent.append(chunk(sentence))
    return chunk_sent

