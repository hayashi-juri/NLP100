""" 39. Zipf's lawPermalink
Plot a log-log graph 
with the x-axis being rank order
and the y-axis being frequency.

>>>
x軸:ランク(1位, 2位, 3位, 4位, ...)
y軸:そのランクに対応する単語の出現頻度(50, 40, 30, 10, ...)
両方の軸を 対数スケール(log-logスケール)でプロット

なぜ log-log スケールを使うのか？
- 自然言語における単語の頻度分布は Zipfの法則 に従う傾向がある。
- Zipfの法則 では、「単語の頻度はランクの逆数に比例する」
    → つまり、順位が高いほど頻度が急激に減少する。
- 通常のスケールで描くと 最頻単語が圧倒的に高くなり、低頻度単語が見えにくくなる。
- log-log スケール にすると、分布が直線に近づき、関係性がわかりやすくなる。
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

frq_num = [w[1] for w in frq.w_frq]
rank = range(1, len(frq_num)+1)

plt.plot(rank, frq_num)
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.xscale("log")
plt.yscale("log")
plt.title("両対数グラフ")
plt.grid(True)
plt.show()