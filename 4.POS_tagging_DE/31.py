""" 31. 動詞
動詞の表層形をすべて抽出せよ
"""
import ttr

verb = set()
for morphs in ttr.result:
    for morph in morphs:
        if morph["pos"] == "VAFIN" or morph["pos"] == "VVFIN":
            # print(dic["surface"])
            verb.add(morph["surface"])

print('動詞の表層形の種類: {}'.format(len(verb)))
print('===10個表示===')
for v in list(verb)[:10]:
    print(v)