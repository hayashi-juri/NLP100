""" 36. 頻度上位10語
出現頻度が高い10語と
その出現頻度をグラフ(例えば棒グラフなど)で表示せよ
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
noun = []

for morphs in m.result:
    for morph in morphs:
        if morph["pos"] != "記号":
            words.append(morph["base"])

        if morph["pos"] == "名詞":
            if morph["base"] == "*\n":
                continue
            else:
                noun.append(morph["base"])

c = Counter(words)
tmp = c.most_common()
w_frq = tmp[:10]
w_10_words = [w[0] for w in w_frq]
w_10_count = [w[1] for w in w_frq]

"""
c = Counter(noun)
tmp = c.most_common()
n_frq = tmp[:10]
n_10_words = [w[0] for w in n_frq]
n_10_count = [w[1] for w in n_frq]

print('===10個表示===')
for frq in n_frq:
    print(frq)
"""

plt.bar(w_10_words, w_10_count)
plt.xlabel('頻出単語')
plt.ylabel('出現頻度')
plt.title('頻出上位10語')  # タイトル
plt.xticks(rotation=45)  # X軸ラベルを45度回転して見やすくする
plt.show()

"""
plt.bar(n_10_words, n_10_count)
plt.xlabel("頻出単語")
plt.ylabel("出現頻度")
plt.title("名詞 上位10頻出単語")
plt.xticks(rotation=45)
plt.show()
"""