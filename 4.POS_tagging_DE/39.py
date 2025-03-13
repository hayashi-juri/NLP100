""" 39. Zipf's lawPermalink
Plot a log-log graph 
with the x-axis being rank order
and the y-axis being frequency.

>>>単語の出現頻度順位を横軸,その出現頻度を縦軸として,
両対数グラフをプロットせよ
38.pyを両対数グラフにする
"""

import frq
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# インストールされた IPAex フォントのパスを確認
font_path = "/usr/share/fonts/opentype/ipaexfont-gothic/ipaexg.ttf"
# フォントプロパティを設定
font_prop = fm.FontProperties(fname=font_path)
# フォントを `matplotlib` に適用
plt.rc('font', family=font_prop.get_name())

frqency = [w[1] for w in frq.w_frq] 

plt.plot(frqency, sorted_frq)
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.xscale("log")
plt.yscale("log")
plt.title("両対数グラフ")
plt.grid(True)
plt.show()