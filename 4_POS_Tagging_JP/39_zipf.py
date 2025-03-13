""" 39. Zipfの法則
単語の出現頻度順位を横軸,その出現頻度を縦軸として,
両対数グラフをプロットせよ
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

c = Counter(words) # 単語とその出現頻度のペアを保持
print(c)
sorted_frq = sorted(c.values(), reverse = True)
# .values() は、その頻度の値（出現回数）のリストを返す
# sorted() は、与えられたリストを昇順または降順に並べ替え
# reverse=True は、並べ替えを降順（大きい順）に指定

ranks = range(1, len(sorted_frq)+1)

plt.plot(ranks, sorted_frq)
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.xscale("log")
plt.yscale("log")
plt.title("両対数グラフ")
plt.grid(True)
plt.show()
