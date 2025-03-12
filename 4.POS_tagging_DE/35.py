""" 35. Frequency of wordsPermalink
Obtain the list of words and frequencies of their occurrences sorted by descending order of frequency.
"""

import gen_morphs
from collections import Counter

words = []

for morphs in gen_morphs.result:
    for morph in morphs:
        if morph["pos"] != "PUNCT" and "SPACE":
            words.append(morph["base"])

c = Counter(words)
frq_word = c.most_common()

print('===10個表示===')
for w in frq_word[:10]:
    print(w)

words_v = []
words_n = []

for morphs in gen_morphs.result:
    for morph in morphs:
        if morph["pos"] == "AUX" or morph["pos"] == "VERB":
            words_v.append(morph["base"])
        elif morph["pos"] == "NOUN":
            words_n.append(morph["base"])

c_v = Counter(words_v)
w_frq_v = c_v.most_common()

c_n = Counter(words_n)
w_frq_n = c_n.most_common()

print('===動詞 5個表示===')
for frq in w_frq_v[:5]:
    print(frq)
print('===名詞 5個表示===')
for frq in w_frq_n[:5]:
    print(frq)
