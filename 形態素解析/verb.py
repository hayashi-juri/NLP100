""" 31. 動詞
動詞の表層形をすべて抽出せよ
"""
import mecab_result as m

verb = set()
for morphs in m.result:
    for morph in morphs:
        if morph["pos"] == "動詞":
            # print(dic["surface"])
            verb.add(morph["surface"])

print('動詞の表層形の種類: {}'.format(len(verb)))
print('===10個表示===')
for v in list(verb)[:10]:
    print(v)


