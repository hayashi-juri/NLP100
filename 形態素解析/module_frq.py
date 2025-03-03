""" 35. 単語の出現頻度
モジュール版
"""
from collections import Counter
import mecab_result as m
# collections.Counter: リストの各要素の数え上げ
# 返り値であるCounterクラスは辞書型

words = []

for morphs in m.result:
    for morph in morphs:
        if morph["pos"] != "記号":
            words.append(morph["base"])
            
c = Counter(words)
w_frequent = c.most_common()
# Counterのmost_common()メソッド
# (要素, 出現回数)を出現回数順に並べたリストを返す
print(w_frequent[:10])
#w_frequent