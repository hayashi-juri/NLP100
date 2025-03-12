""" 34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import gen_morphs

noun_phrase = set()
noun_tmp = []
for morphs in gen_morphs.result:
    for morph in morphs:
        if morph["pos"] == "NOUN":
            noun_tmp.append(morph["surface"])
        else:
            if len(noun_tmp) > 1:
                noun_phrase.add(" ".join(noun_tmp))
                noun_tmp = []

print('名詞句の総数: {}'.format(len(noun_phrase)))
print('===10個表示===')
for np in list(noun_phrase)[:10]:
    print(np)
