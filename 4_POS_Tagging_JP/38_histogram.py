""" 38. ヒストグラム
単語の出現頻度のヒストグラムを描け
ただし
- 横軸は出現頻度
- 1から単語の出現頻度の最大値までの線形目盛

縦軸はx軸で示される出現頻度となった単語の異なり数(種類数)である
"""
from collections import Counter
import mecab_result as m
import matplotlib.pylab as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

words = []
for morphs in m.result:
    for morph in morphs:
        if morph["pos"] != "記号":
            words.append(morph["base"])

c = Counter(words) # 全体の単語数
frq = c.values() # 値の一覧を取得する

#plt.hist(frq, bins = 100) # 階級（ヒストグラムの棒）の数
plt.hist(frq, range(1, 30)) 
plt.xlabel("出現頻度")
plt.ylabel("種類数")
plt.title("ヒストグラム")
plt.grid(True)
plt.show()
