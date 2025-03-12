import gen_morphs
from collections import Counter

words = []

for morphs in gen_morphs.result:
    for morph in morphs:
        if morph["pos"] != "PUNCT" and "SPACE":
            words.append(morph["base"])

c = Counter(words)
w_frq = c.most_common()

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

w_frq
w_frq_v
w_frq_n
