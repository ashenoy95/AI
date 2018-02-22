from nltk.corpus import brown
from nltk.util import ngrams
from collections import Counter, defaultdict
import pandas as pd

sentence = 'time flies like an arrow'
words = sentence.split().

tokens, tags = zip(*brown.tagged_words())

tagCounter = Counter(tags)

tokenTags = defaultdict(Counter)
for token, tag in brown.tagged_words():
    tokenTags[token][tag] +=1
    
tagTags = defaultdict(Counter)
posBigrams = list(ngrams(tags, 2))
for tag1, tag2 in posBigrams:
    tagTags[tag1][tag2] += 1

df = pd.DataFrame(index=set(tags), columns=['init']+words)

offset = 0
initialTags = Counter()
for x in brown.sents():
    initTag = tags[offset]
    initialTags[initTag] += 1
    offset += len(x)

df['init'] = df.apply(lambda x: initialTags[x.name]/len(tags), axis=1)
            
for col in range(1, len(words)+1):
    for row in range(len(set(tags))):
        p = 0
        token = df.columns[col]
        currentTag = df.iloc[row].name
        for row2 in range(len(set(tags))):
            prevTag = df.iloc[row2].name
            p += (tagTags[prevTag][currentTag]/tagCounter[prevTag])*(df.iloc[row2,col-1])*(tokenTags[token][currentTag]/tagCounter[currentTag])
        df.iloc[row,col] = p

for word in words:
    print(df[word].argmax(), end=' ')

