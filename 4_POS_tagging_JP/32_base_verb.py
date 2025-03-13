""" 32. 動詞の基本形
動詞の基本形をすべて抽出せよ
"""
import mecab_result as m

verb_base = set()

for morphs in m.result:
    for morph in morphs:
        if morph["pos"] == "動詞":
            verb_base.add(morph["base"])

print('動詞の基本形の種類: {}'.format(len(verb_base)))
print('===10個表示===')
for v in list(verb_base)[:10]:
    print(v)