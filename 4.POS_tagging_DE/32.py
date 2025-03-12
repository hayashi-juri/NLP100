"""32. 動詞の基本形
動詞の基本形をすべて抽出せよ
"""
import gen_morphs

verb = set()
for morphs in gen_morphs.result:
    for morph in morphs:
        if morph["pos"] == "AUX" or morph["pos"] == "VERB":
            verb.add(morph["base"])

print('動詞の基本形の種類: {}'.format(len(verb)))
print('===10個表示===')
for v in list(verb)[:10]:
    print(v)