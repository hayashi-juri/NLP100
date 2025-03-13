""" 37. 「猫」と共起頻度の高い上位10語
「猫」とよく共起する(共起頻度が高い)10語と
その出現頻度をグラフ(例えば棒グラフなど)で表示せよ．
"""
from collections import Counter
import mecab_result as m
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

words = []
without = ["記号", "助詞", "助動詞", "補助記号"] # 補助記号、助詞、助動詞を除外

for morphs in m.result:
    for morph in morphs:
        if "猫" in [x["surface"] for x in morphs]:
            for morph in morphs:
                if morph["pos"] not in without and morph["base"] != "猫" and morph["base"] != "*\n":
                    words.append(morph["base"]) # 文中の単語をリストにする

c = Counter(words)
frq_10 = c.most_common(10)
cat_10_words = [w[0] for w in frq_10]
cat_10_count = [w[1] for w in frq_10]
print(frq_10)

plt.bar(cat_10_words, cat_10_count)
plt.xlabel('頻出単語')
plt.ylabel('出現頻度')
plt.title("「猫」と共起頻度の高い上位10語")  # タイトル
plt.xticks(rotation=45)  # X軸ラベルを45度回転して見やすくする
plt.show()



