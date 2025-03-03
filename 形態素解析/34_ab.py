""" 34. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

import mecab_result as m

noun_phrase = set()

for morphs in m.result:
    word = [] # 現在の名詞句を格納するリスト
    for morph in morphs:
        if morph["pos"] == "名詞": 
            word.append(morph["surface"])

        else: # 名詞でない場合の処理
            if len(word) > 1:
                # morph が名詞でない場合、
                # 現在までの word が1語以上の名詞を含んでいるとき
                # word を1つの名詞句としてセットに追加
                noun_phrase.add("".join(word))
                word = [] # リセット

# 結果の表示
print('名詞句の総数: {}'.format(len(noun_phrase)))
print('===10個表示===')
for np in list(noun_phrase)[:10]:
    print(np)