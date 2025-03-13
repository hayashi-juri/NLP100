""" 37. Top-ten words co-occurring with "Märchen" and "Wolf". 
Extract the list of words that co-occur with the word "Märchen" and "Wolf". 
Visualize with a chart (e.g., bar chart) the top-ten words co-occurring with the word "Märchen", "Wolf" and their frequencies.

「Märchen」, 「Wolf」とよく共起する(共起頻度が高い)10語と
その出現頻度をグラフ(例えば棒グラフなど)で表示せよ．
"""

from collections import Counter
import gen_morphs
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

words_m = [] # Märchen
words_w = [] # Wolf
without = ["PUNCT", "SPACE"]

for morphs in gen_morphs.result:
    # search "Märchen" related words
    if "Märchen" in [w["surface"] for w in morphs]:
        for morph in morphs:
            if morph["pos"] not in without and morph["base"] != "Märchen":
                words_m.append(morph["base"])
    # serch "Wolf" related words
    elif "Wolf" in [w["surface"] for w in morphs]:
        for morph in morphs:
            if morph["pos"] not in without and morph["base"] != "Wolf":
                words_w.append(morph["base"])

# graph preparation for "Märchen"
c = Counter(words_m)
frq_10 = c.most_common(10)
m_w = [w[0] for w in frq_10]
m_c = [w[1] for w in frq_10]
##print(frq_10)

# graph preparation for "Wolf"
c = Counter(words_w)
frq_10 = c.most_common(10)
w_w = [w[0] for w in frq_10]
w_c = [w[1] for w in frq_10]

plt.bar(m_w, m_c)
plt.xlabel('頻出単語')
plt.ylabel('出現頻度')
plt.title("「Märchen」と共起頻度の高い上位10語")  # タイトル
plt.xticks(rotation=45)  # X軸ラベルを45度回転して見やすくする
plt.show()

plt.bar(w_w, w_c)
plt.xlabel('頻出単語')
plt.ylabel('出現頻度')
plt.title("「Wolf」と共起頻度の高い上位10語")  # タイトル
plt.xticks(rotation=45)  # X軸ラベルを45度回転して見やすくする
plt.show()

